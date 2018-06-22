#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MorainWebsite.settings")  # project_name 项目名称
django.setup()
from library.models import Section, Novel
from bs4 import BeautifulSoup
import requests
import re
from db_tools import cn2dig


# from apscheduler.schedulers.blocking import BlockingScheduler

# sched = BlockingScheduler()


# def getUpdateCount():
#     def wrapper(*args, **kw):


# 通过url获取网页内容
def getPage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Cookie': 'UM_distinctid=160452b6ed034e-01649f85eacc67-16386656-1fa400-160452b6ed181b; CNZZDATA1263990213=176387233-1512987067-https%253A%252F%252Fwww.baidu.com%252F%7C1512987067',
        'Host': 'www.23us.so',
        'X-Requested-With': 'XMLHttpRequest',
    }
    return requests.get(url, headers=headers).content


# 通过小说名称获取小说地址
def getNovelUrl(title):
    url = 'http://zhannei.baidu.com/cse/search?q={}&click=1&entry=1&s=5513259216532962936&nsid='.format(title)
    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')
    novel_url = soup('a', cpos='title')[0].get('href')
    return novel_url


# 通过小说在网站的ID以及名称获取Novel对象，包含标题，作者，状态，总字数，最近一次更新日期
def getNovel(id):
    data = getPage('http://www.23us.so/xiaoshuo/{}.html'.format(id))
    soup = BeautifulSoup(data, 'html.parser')

    abstract = soup('table', width="740px", cellpadding="0", cellspacing="0")[0].find_next("p").text
    img_src = soup.find('a', class_='hst').find('img')['src']
    info = soup('td')
    type = info[0].text.strip()
    author = info[1].text.strip()
    state = info[2].text.strip()
    count_word = re.sub("\D", "", info[4].text.strip())
    novel = Novel(author=author, abstract=abstract,
                  count_word=count_word, state=state, novel_image=img_src, type=type)
    return novel


# 导入Section
def AddSections(novel):
    novel_section_list = []
    page_novel = getPage(novel.novel_url)  # 获取小说章节列表
    soup = BeautifulSoup(page_novel, 'html.parser')
    section_list = soup('td', class_="L")
    for sec in section_list:
        section_title = sec.get_text()
        section_url = sec.a.get('href')
        re_num = re.search(u'第(.*?)章', section_title)
        other_num = str(section_title.split(' ')[0]).isdigit()
        if re_num or other_num:
            try:
                num = re_num.group(1)
                if num.isdigit():
                    num = int(num)
                else:
                    num = cn2dig(num)
                if other_num:
                    num = other_num
            except Exception:
                num = None
            section = Section(num=num)
            page = getPage(section_url)
            soup = BeautifulSoup(page, 'html.parser')
            section_content = str(soup.find('dd', id="contents"))
            print("正在将 {} 打包".format(section_title), num)
            section.title = section_title
            section.section_url = section_url
            section.content = section_content
            section.novel = novel
            # section.save()
            novel_section_list.append(section)
    Section.objects.bulk_create(novel_section_list)
    print("已添加" + str(len(novel_section_list)) + "章节")

    return novel_section_list


def UpdateSections(novel_list):
    for novel in novel_list:
        novel_section_list = []
        page_novel = getPage(novel.novel_url)  # 获取小说章节列表
        soup = BeautifulSoup(page_novel, 'html.parser')
        section_list = reversed(soup('td', class_="L"))  # 从最新的章节开始爬取
        for sec in section_list:
            section_title = sec.get_text()
            section_url = sec.a.get('href')
            # re_num = re.search(u'第(.*?)章', section_title)
            # other_num = str(section_title.split(' ')[0]).isdigit()
            #     try:
            #         num = re_num.group(1)
            #         if num.isdigit():
            #             num = int(num)
            #         else:
            #             num = cn2dig(num)
            #         if other_num:
            #             num = other_num
            #     except Exception:
            #         num = None
            section = Section()
            page = getPage(section_url)
            soup = BeautifulSoup(page, 'html.parser')
            section_content = str(soup.find('dd', id="contents"))
            if Section.objects.filter(title=section_title, section_url=section_url, novel_id=novel.id).exists():
                novel_section_list.reverse()
                for s in novel_section_list:
                    print(s)
                    s.save()
                print(novel.title + "更新结束。")
                break
            #         return len(novel_section_list)
            else:
                section.title = section_title
                section.section_url = section_url
                section.content = section_content
                section.novel_id = novel.id
                # print("正在将 {} 打包".format(section_title), num)
                # print("正在保存 {}".format(section_title), num)
                # section.save()
                # novel_section_list.insert(0, section)
                novel_section_list.append(section)
                # print(section_title)
        # Section.objects.bulk_create(novel_section_list)
        # print("已添加 " + str(len(novel_section_list)) + " 章节")
        # novel_section_list.reverse()
        # for s in novel_section_list:
        #     print(s)
        #     s.save()


def load_novel(novel_title_list):
    for title in novel_title_list:
        # 获取小说url与标题组成元组并添加成列表
        novel_url = getNovelUrl(title)
        # novel_tuple_list.append((novel_url, title))  # (novelurl,noveltitle)
        # 正则连接样式，获取小说id
        relink = 'http://www.23us.so/files/article/html/.*?/(.*?)/index.html'
        id = re.match(relink, novel_url).group(1)
        if id:
            # 获取小说主信息
            novel = getNovel(id)
            novel.title = title
            novel.novel_url = novel_url
            # novel.add_user_id = user_id
            # 获取小说对象
            # 判断小说是否存在
            # 存在则更新信息
            # 不存在则加入novel_info_list列表等待添加
            if Novel.objects.filter(novel_url=novel.novel_url).exists():
                # Novel.objects.filter(novel_url=novel.novel_url).update(author=novel.author,
                #                                                        count_word=novel.count_word, state=novel.state,
                #                                                        type=novel.type)
                update_num = UpdateSections(Novel.objects.get(novel_url=novel.novel_url))
            else:
                novel.save()
                print(novel.title, "已添加")
                load_num = AddSections(novel)

                # length = len(novel_section_list)
                # n = length // 200
                # for i in range(n):
                #     part_section_list = novel_section_list[i * 200: i * 200 + 200]
                #     Section.objects.bulk_create(part_section_list)
                # Section.objects.bulk_create(novel_section_list[-(length - n * 200):])


# @sched.scheduled_job('interval', seconds=60)
# def mytask():
#     novel_title_list = ['宠物天王', '修真聊天群', '寒门崛起', '龙王传说', '圣墟', ]
#     load_novel(novel_title_list)
#
#
# def startsched():
#     sched.start()


if __name__ == '__main__':
    # startsched()
    # Novel.objects.raw("TRUNCATE TABLE novel_section;")
    # Novel.objects.raw("TRUNCATE TABLE novel_novel;")
    # print(len(Section.objects.all()))

    novel_title_list = ['宠物天王', '修真聊天群', '寒门崛起', '龙王传说', '圣墟', '放开那个女巫', '全职法师', '神级强者在都市', '剑来', '大王饶命', '异常生物见闻录']
    # # novel_title_list = ['修真聊天群']
    load_novel(novel_title_list)

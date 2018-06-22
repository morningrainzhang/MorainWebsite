# Scrapy
## 创建虚拟环境
virtualenv novelspider
deactivate
## 创建项目
```
cd /Users/zhangchenyu/PycharmProjects/Scrapy 
scrapy3 startproject novelspider
scrapy3 genspider dindian www.23us.so#创建爬虫
scrapy3 crawl novelspider

```
## 创建启动PY
main.py

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from scrapy.cmdline import execute
	import os
	import cmd
	#执行命令，相当于在控制台cmd输入改名了
	
	spiders = [
	    # 'scrapy genspider novelspider www.23us.so',
	    'scrapy crawl novelspider',
	]
	
	if __name__ == '__main__':
	    print(os.path.abspath(__file__))
	    for i in spiders:
	        execute(i.split())
## 配置setting.py

### 设置django环境
#### 方法一
	# init django environment
	import os, django
	import sys
	
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	sys.path.append(BASE_DIR)
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "novel.settings")
	django.setup()
#### 方法二
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	def setup_django_env():
	    import os, sys, django
	    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	    sys.path.append(BASE_DIR)
	    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "novel.settings")
	    django.setup()
	
	
	def check_db_connection():
	    from django.db import connection
	
	    if connection.connection:
	        if not connection.is_usable():
	            connection.close()
## 使用django的ORM
安装scrapy_djangoitem

`from scrapy_djangoitem import DjangoItem`
### items.py
	import scrapy
	from novelapp.models import Novel,Section
	from scrapy_djangoitem import DjangoItem
	from novelapp.models import Novel, Section
	
	
	class NovelItem(DjangoItem):
	    django_model = Novel
	
	
	class SectionItem(DjangoItem):
	    django_model = Section
### spider中地址传递
#### 方法一
1. yield scrapy.Request(detail_href, callback=self.parse_detail, meta={'url': novel_url})
2. yield scrapy.Request(response.meta['url'], callback=self.parse_item, meta={'novel': novelitem})
3. yield scrapy.Request(url, callback=self.section_item, meta={'novel': response.meta['novel']})

dingdian.py

```
class NovelSpider(scrapy.Spider):
    name = 'dingdian'
    allowed_domains = ['www.23us.so']
    start_urls = []
    novel_title_list = ['宠物天王', '修真聊天群', '寒门崛起', '龙王传说']
    for title in novel_title_list:
        url = 'http://zhannei.baidu.com/cse/search?q={}&click=1&entry=1&s=5513259216532962936&nsid='.format(title)
        start_urls.append(url)

    def parse(self, response):
        # 获取小说地址及作者
        novel_url = response.xpath('//h3[@class="result-item-title result-game-item-title"]/a/@href').extract_first()
        # novel_auther = response.xpath('//p[@class="result-game-item-info-tag"]/span/text()').extract()[1].strip()
        # 从地址提取小说在顶点的id
        relink = 'http://www.23us.so/files/article/html/.*?/(.*)/index.html'
        id = re.findall(relink, novel_url)[0]
        detail_href = 'http://www.23us.so/xiaoshuo/{}.html'.format(id)
        yield scrapy.Request(detail_href, callback=self.parse_detail, meta={'url': novel_url})

    def parse_detail(self, response):
        title = response.xpath('//dl[@id="content"]/dd/h1/text()').extract_first().split(' ')[0]
        detail = response.xpath('//table[@id="at"]/tr/td')
        type = detail[0].xpath('a/text()').extract_first().split()[0]
        author = detail[1].xpath('text()').extract_first().split()[0]
        state = detail[2].xpath('text()').extract_first().split()[0]
        count_word = re.sub("\D", "", detail[4].xpath('text()').extract_first())[0]
        abstract = response.xpath('//dd[@style="padding:10px 30px 0 25px;"]/p[2]')[0].extract()
        novelitem = NovelItem(title=title, type=type, author=author, abstract=abstract,
                              count_word=count_word, state=state)
        yield scrapy.Request(response.meta['url'], callback=self.parse_item, meta={'novel': novelitem})
        yield novelitem

    def parse_item(self, response):
        section_url = response.xpath('//table[@id="at"]/tr/td[@class="L"]/a/@href').extract()
        # 根据章节标题筛选
        # section_title = list(filter(lambda title: u'章' in title,section_title))
        for url in section_url:
            yield scrapy.Request(url, callback=self.section_item, meta={'novel': response.meta['novel']})

    def section_item(self, response):
        section_title = response.xpath('//div[@id="amain"]/dl/dd/h1/text()').extract_first()
        section_content = response.xpath('//dd[@id = "contents"]').extract_first()
        if len(section_content) > 2000:
            print(type(response.meta['novel']))
            yield SectionItem(title=section_title, content=section_content, novel=response.meta['novel'])
```

#### 方法二
### 数据保存

dingdian.py

```
    # 爬取小说目录并返回item
    def parse_item(self, response):
        section_url = response.xpath('//table[@id="at"]/tr/td[@class="L"]/a/@href').extract()
        print(section_url)
        print(len(response.xpath('//div[@id="amain"]/dl/dd/h1/text()')))
        if len(response.xpath('//div[@id="amain"]/dl/dd/h1/text()')) == 0:
            for url in section_url:
                yield scrapy.Request(url, callback=self.parse_item, meta={'novel': response.meta['novel']})
        section_title = response.xpath('//div[@id="amain"]/dl/dd/h1/text()').extract_first()
        section_content = response.xpath('//dd[@id = "contents"]').extract_first()
        if len(section_content) > 2000:
            item = {}
            item['novel'] = response.meta['novel']
            item['section'] = SectionItem(title=section_title, content=section_content)
            yield item
```

pipelines.py

```
class NovelspiderPipeline(object):
    def process_item(self, item, spider):
        # 检查数据库内是否已经存在该小说
        def _check_novel(novel_title):
            try:
                ins = Novel.objects.get(title=novel_title)
                return ins
            except:
                return None

        # 分发 dict
        if isinstance(item, dict):
            # 提取 两个 ITEM
            novel = item['novel']
            section = item['section']
            novel_title = novel['title']
            sections_ = 0
            # 判断该小说是否存在
            if _check_novel(novel_title):
                novel = _check_novel(novel_title)
                sections_ = len(novel.section_set.filter(title=section['title']))
            # 保存小说
            novel.save()

            # 判断该小说章节是否有重复
            if sections_ == 0:
                section['novel'] = Novel.objects.get(title=novel_title)
                section.save()

            return item
```

### 取消ROBOT协议

`ROBOTSTXT_OBEY = False`

### 部署Scrapyd
scrapyd-deploy
curl http://localhost:6800/schedule.json -d project=novelspider -d spider=dingdian

### bug
service_identity 版本太老
`pip3 install service_identity --force --upgrade`

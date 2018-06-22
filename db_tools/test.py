import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MorainWebsite.settings")
django.setup()
from django.core.mail import send_mail
from MorainWebsite.settings import EMAIL_HOST_USER
from library.models import UserFav, Section, Novel
from django.core.mail import EmailMessage, EmailMultiAlternatives


def send():
    email_list = []
    section = Section.objects.first()
    novel = section.novel
    # print(section.content)
    content = """
    这是{}的更新。
    乖~
    快看
    http://www.morainz.com/detail/{}/
    """.format(novel.title, section.id)
    user_fav_list = UserFav.objects.filter(novel=novel).select_related('user')
    print(123)
    # for user_fav in user_fav_list:
    #     # email_list.append(user_fav.user.email)
    #     user_fav.user.email_user(section.novel.title + "-" + section.title, content,
    #                              EMAIL_HOST_USER)
    # html_content = '<p>这是一封<strong>重要的</strong>邮件.</p>'
    # msg = EmailMultiAlternatives(section.novel.title+"更新咯~", html_content+section.content, EMAIL_HOST_USER, email_list)
    # # msg.attach_alternative(html_content, "text/html")
    # msg.attach_alternative(section.content, "text/html")
    #
    # msg.send()
    # send_mail("标题", section.content, EMAIL_HOST_USER, email_list)


def res():
    for i in [1,2,3]:
        for j in [4,5,6]:
            if j==5:
                continue
            else:
                print(i,j)


if __name__ == '__main__':
    # send()
    res()

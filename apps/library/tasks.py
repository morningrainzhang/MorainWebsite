from celery import task, shared_task
from db_tools.addnovel import UpdateSections
from library.models import Novel, Section
from django.core.mail import send_mail
from MorainWebsite.settings import EMAIL_HOST_USER


@task()
def helloworld():
    print('hello world')


@task()
def update_novel():
    novel_list = Novel.objects.all()
    UpdateSections(novel_list)
        # print(novel.title + "已更新" + str(l) + "章节")


@task()
def send_email_fav():
    send_mail("标题", "内容", EMAIL_HOST_USER, ['799842527@qq.com'])
    return 123

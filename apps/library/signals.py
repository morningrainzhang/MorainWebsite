# encoding: utf-8
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from MorainWebsite.settings import EMAIL_HOST_USER
from django.contrib.auth import get_user_model
from library.models import UserFav, Section

User = get_user_model()


# 参数一接收哪种信号，参数二是接收哪个model的信号
@receiver(post_save, sender=UserFav)
def create_user_fav(sender, instance=None, created=False, **kwargs):
    # 是否新建，因为update的时候也会进行post_save
    if created:
        send_mail("标题", "内容", EMAIL_HOST_USER, ['799842527@qq.com'])
        novel = instance.novel
        novel.fav_num += 1
        novel.save()


# 参数一接收哪种信号，参数二是接收哪个model的信号
@receiver(post_delete, sender=UserFav)
def del_user_fav(sender, instance=None, created=False, **kwargs):
    novel = instance.novel
    novel.fav_num -= 1
    novel.save()


# 参数一接收哪种信号，参数二是接收哪个model的信号
@receiver(post_save, sender=Section)
def create_section(sender, instance=None, created=False, **kwargs):
    if created:
        # send_mail("标题", "内容", EMAIL_HOST_USER, ['17858935980@163.com'])
        # send_mail("标题", "内容", EMAIL_HOST_USER, ['morainz@126.com'])
        section = instance
        novel = section.novel
        # print(section.content)
        content = """
        这是{}的更新。
        乖~
        快看
        http://www.morainz.com/detail/{}/
        """.format(novel.title, section.id)
        user_fav_list = UserFav.objects.filter(novel=novel).select_related('user')
        for user_fav in user_fav_list:
            # email_list.append(user_fav.user.email)
            user_fav.user.email_user(section.novel.title + "-" + section.title, content,
                                     EMAIL_HOST_USER)

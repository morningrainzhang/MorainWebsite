import os
from celery import Celery
from django.conf import settings

# 设置运行环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MorainWebsite.settings')
# 实例化一个Celery
app = Celery('MorainWebsite')
# 设置celery配置文件(MorainWebsite/settings.py)
app.config_from_object('django.conf:settings')
# 自动发现位于INSTALLED_APPS中app里面的task任务
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

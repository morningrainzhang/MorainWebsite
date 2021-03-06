"""
Django settings for MorainWebsite project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import datetime
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=(a1g*ez5*&jj(+h7=da&do6+#e54q*peg@qlr=p80(ju6kz=o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
APPEND_SLASH = False
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'library.apps.LibraryConfig',
    'blog.apps.BlogConfig',
    'gallery.apps.GalleryConfig',
    'one.apps.OneConfig',
    # xadmin
    'xadmin',
    'crispy_forms',
    # 编辑器
    'DjangoUeditor',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    # 跨域
    # 'corsheaders'
    'simditor',
    # 异步 定时
    'djcelery',
    # 缩略图
    'easy_thumbnails'
]
AUTH_USER_MODEL = "users.UserProfile"
# Application definition


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 允许跨域
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'MorainWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MorainWebsite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moraindb',
        'USER': 'root',
        # local
        # 'HOST': '127.0.0.1',
        # 'PASSWORD': '!qaz@wsx#edc123',
        # tengxun
        'PASSWORD': 'hz123456',
        'HOST': '118.25.22.152',

        "OPTIONS": {"init_command": "SET default_storage_engine=INNODB;"}
    }
}
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# 语言改为中文
LANGUAGE_CODE = 'zh-hans'

# 时区改为上海
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# 配置邮箱发送者
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # email后端
# EMAIL_USE_TLS = True  # 是否使用TLS安全传输协议
# qq邮箱
# EMAIL_USE_SSL = True     #是否使用SSL加密，qq企业邮箱要求使用
# EMAIL_HOST = 'smtp.qq.com'  # 发送邮件的邮箱 的 SMTP服务器，这里用了qq企业邮箱
# EMAIL_PORT = 25  # 发件箱的SMTP服务器端口
# EMAIL_HOST_USER = 'mail@morainz.com'  # 发送邮件的邮箱地址
# EMAIL_FROM = 'mail@morainz.com'  # 你的QQ账号
# EMAIL_HOST_PASSWORD = 'pnavvpohlfidbedj'  # 发送邮件的邮箱密码

# 126邮箱
EMAIL_HOST = 'smtp.126.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'morainz@126.com'
EMAIL_HOST_PASSWORD = 'ZCYhz123456'
FROM_EMAIL = 'Morain <www.morainz.com>'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# VERIFICATIONCODELENGTH = 4

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# THUMB_ROOT = os.path.join(BASE_DIR, "media")

AUTHENTICATION_BACKENDS = (
    'users.apiviews.CustomBackend',

)

# 所有与drf相关的设置写在这里面
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10000/day',
        'user': '100000/day'
    }
}

# 与drf的jwt相关的设置
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3600),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

# blog编辑器
SIMDITOR_UPLOAD_PATH = 'uploads/'
SIMDITOR_IMAGE_BACKEND = 'pillow'

SIMDITOR_TOOLBAR = [
    'title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale',
    'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|', 'link',
    'image', 'hr', '|', 'indent', 'outdent', 'alignment', 'fullscreen',
    'markdown', 'emoji'
]

SIMDITOR_CONFIGS = {
    'toolbar': SIMDITOR_TOOLBAR,
    'upload': {
        'url': '/simditor/upload/',
        'fileKey': 'upload'
    },
    'emoji': {
        'imagePath': '/static/simditor/images/emoji/'
    }
}

# 缩略图
THUMBNAIL_ALIASES = {
    '': {
        'gallery': {'size': (355, 237), 'crop': True},
        'blog': {'size': (300, 200), 'crop': True},
    },
}

# celery任务调度
import djcelery

djcelery.setup_loader()
# 设置中间件为redis，也就是使用redis进行任务队列管理。
BROKER_URL = 'redis://127.0.0.1:6379/2'
# 选取在名称为library的app中的任务(在app下创建tasks.py)
CELERY_IMPORTS = ('library.tasks',)
# 失去上海，与django的失去保持一致
CELERY_TIMEZONE = 'Asia/Shanghai'
# 这是使用了django-celery默认的数据库调度模型, 任务执行周期都被存在你指定的orm数据库中
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# 选择指定的orm数据库进行操作
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
# 这个是任务预取功能，就是每个工作的进程／线程／绿程在获取任务的时候，会尽量多拿 n 个，以保证获取的通讯成本可以压缩,因为我们的小说更新不需要并发，所以选取1
CELERYD_PREFETCH_MULTIPLIER = 1
worker_prefetch_multiplier = 1
# 丢弃结果配置
CELERY_IGNORE_RESULT = True
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

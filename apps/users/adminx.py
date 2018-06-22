# encoding: utf-8

import xadmin
from xadmin import views
from .models import EmailVerifyRecord


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "MORAIN"
    site_footer = "http://www.morainz.com"
    menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ['code', 'email', 'send_type', 'add_time']


xadmin.site.register(EmailVerifyRecord, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

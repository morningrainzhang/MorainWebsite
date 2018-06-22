import xadmin
from library.models import Novel, Section, UserFav


class NovelAdmin(object):
    list_display = ["title", "state", "author", "type", "count_word", "abstract",
                    "novel_image", "add_time", "novel_url", ]
    search_fields = ['title', "author"]
    list_editable = ["is_hot", ]
    list_filter = ["title", "state", "author", "type", "count_word", "abstract",
                   "novel_image", "add_time", "novel_url", ]
    style_fields = {"novels_desc": "ueditor"}


class SectionAdmin(object):
    list_display = ["novel", "title", "num", "add_time", "section_url"]
    search_fields = ["title", "novel__title"]
    list_filter = ["novel"]


class UserFavAdmin(object):
    list_display = ["user", "novel", "add_time"]
    search_fields = ['user__username', "novel__title"]
    list_filter = ["user", "novel", "add_time"]


xadmin.site.register(Novel, NovelAdmin)
xadmin.site.register(Section, SectionAdmin)
xadmin.site.register(UserFav, UserFavAdmin)

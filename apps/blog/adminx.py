import xadmin
from blog.models import ArticleType, ArticleTag, Article


class ArticleAdmin(object):
    list_display = ["title", "describe","tags", "article_type", "article_image", "author", "create_time", ]
    search_fields = ['title', "tags", "article_type", ]
    list_editable = ['title',"describe", "article_image", "tags", "article_type", "create_time", ]
    list_filter = ["title", "author", "tags", "article_type", "create_time", ]


class ArticleTagAdmin(object):
    list_display = ("tag_name",)
    search_fields = ["tag_name", ]
    list_filter = ["tag_name", ]


class ArticleTypeAdmin(object):
    list_display = ["type_name", ]
    search_fields = ["type_name", ]
    list_filter = ["type_name", ]


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(ArticleTag, ArticleTagAdmin)
xadmin.site.register(ArticleType, ArticleTypeAdmin)

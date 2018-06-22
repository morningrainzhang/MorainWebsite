from django.contrib import admin
from .models import ArticleType, ArticleTag, Article


# Register your models here.
@admin.register(ArticleType)
class ArcticleTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'type_describe')


@admin.register(ArticleTag)
class ArcticleTagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)


@admin.register(Article)
class ArcticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'describe', 'update_time', 'is_deleted')
    ordering = ("id",)

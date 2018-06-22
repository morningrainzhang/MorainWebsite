from django.contrib import admin
from gallery.models import Image, ImageType


# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('img_type', 'image', 'name', 'create_time',)
    list_per_page = 20
    ordering = ("-create_time",)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('img_type', 'name',)

    list_filter = ('img_type', 'create_time')  # 过滤器
    # search_fields = ('caption', )          #搜索字段
    # date_hierarchy = 'publish_time'        #详细时间分层筛选


@admin.register(ImageType)
class ImageTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'type_describe', 'type_image')

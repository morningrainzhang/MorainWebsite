import xadmin
from gallery.models import Image, ImageType


class ImageTypeAdmin(object):
    list_display = ["type_name", "type_describe", "type_image", ]
    list_editable = ["type_name", "type_describe", "type_image", ]
    search_fields = ["type_name", "type_describe"]


class ImageAdmin(object):
    list_display = ["name", "describe", "image", "create_time", "update_time", "user",
                    "img_type", ]
    search_fields = ['name', "user", "img_type", ]
    list_editable = ["img_type", "name", "describe", ]
    list_filter = ["name", "user", "img_type", "create_time", ]


xadmin.site.register(ImageType, ImageTypeAdmin)
xadmin.site.register(Image, ImageAdmin)

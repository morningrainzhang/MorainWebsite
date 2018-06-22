import os
from django.db import models
# from django.db.models.fields.files import ImageFieldFile
from django.contrib.auth import get_user_model
# from MorainWebsite.settings import MEDIA_ROOT

from easy_thumbnails.fields import ThumbnailerImageField
User = get_user_model()


# Create your models here.


class ImageType(models.Model):
    type_name = models.CharField(max_length=50, null=True, verbose_name='相册名称')
    type_describe = models.CharField(max_length=200, null=True, verbose_name='相册类型介绍')
    type_image = models.ImageField(upload_to='image/type/', verbose_name='相册封面')

    class Meta:
        verbose_name = '相册类型'
        verbose_name_plural = '相册类型'

    def __str__(self):
        return self.type_name


# def make_thumb(path, size = 480):
#     pixbuf = Image.open(path)
#     width, height = pixbuf.size
#
#     if width > size:
#         delta = width / size
#         height = int(height / delta)
#         pixbuf.thumbnail((size, height), Image.ANTIALIAS)


class Image(models.Model):
    image = ThumbnailerImageField(upload_to='image/', blank=True, verbose_name='图片地址')
    # thumb = models.ImageField(upload_to='image/thumb', blank=True, verbose_name=' 缩略图地址')
    name = models.CharField(max_length=50, null=True, verbose_name='图片名称')
    describe = models.CharField(max_length=200, null=True, verbose_name='图片描述')
    create_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name='图片创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name='图片更新时间')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='所属人')
    img_type = models.ForeignKey(ImageType, on_delete=models.CASCADE, default=1, verbose_name='所属类型')

    # def save(self):
    #     super(Image, self).save()  # 将上传的图片先保存一下，否则报错
    #     base, ext = os.path.splitext(os.path.basename(self.image.path))
    #     thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, self.image.name))
    #     relate_thumb_path = os.path.join(THUMB_ROOT, base + '.thumb' + ext)
    #     thumb_path = os.path.join(MEDIA_ROOT, relate_thumb_path)
    #     thumb_pixbuf.save(thumb_path)
    #     self.thumb = ImageFieldFile(self, self.thumb, relate_thumb_path)
    #     super(Image, self).save()
    #     #再保存一下，包括缩略图等

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '图库'
        verbose_name_plural = '图库'
        ordering = ['-create_time']

import django
import os
from MorainWebsite.settings import MEDIA_ROOT

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MorainWebsite.settings")
django.setup()
from random import choice
from gallery.models import *

if __name__ == '__main__':
    # print(os.listdir(path))
    dir = (MEDIA_ROOT + "/image")
    for filename in os.listdir(dir):
        image = Image()
        apath = os.path.join("image", filename)
        if len(filename)<50:
            image.image = apath
            image.describe = filename + "测试图片已上传！！！"
            image.name = filename
            image.img_type = choice(ImageType.objects.all())
            image.save()
        # image/201802/28/DSCF5702.JPG

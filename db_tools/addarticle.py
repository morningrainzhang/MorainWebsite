import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MorainWebsite.settings")
django.setup()
from MorainWebsite.settings import MEDIA_ROOT
from blog.models import *
from gallery.models import *
from random import choice


def addarticlebylocal():
    for i in range(98):
        article = Article()
        article.title = "for %s" % i
        article.describe = "测试文章 %s" % i
        article.content = "xxxx:%s" % i
        article_type = ArticleType.objects.all()[0]
        article.article_type = article_type
        article.article_image = choice(Image.objects.all()).image
        article.save()

    articles = Article.objects.all()
    print(articles.count())


# print(choices(Image.objects.all(),k=2))

def addarticlebymarkdown():
    dir = os.path.join(MEDIA_ROOT + "/markdown")
    for filename in os.listdir(dir):
        mfile = open(os.path.join(dir, filename), 'r').read()
        filename = filename.split('.')[0]
        article = Article()
        article.title = filename
        article.describe = filename
        article.content = mfile
        article_type = choice(ArticleType.objects.all())
        article.article_type = article_type
        article.article_image = choice(Image.objects.all()).image
        article.save()


if __name__ == '__main__':
    addarticlebymarkdown()
    # addarticlebymarkdown

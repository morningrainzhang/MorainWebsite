from blog.models import *
from django import template
import random
from django.db.models.aggregates import Count

register = template.Library()


@register.simple_tag
def get_recent_articles(num=5):
    return Article.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def get_random_articles(num=4):
    # article_list = list(Article.objects.values_list('id', flat=True))
    article_list = list(Article.objects.all())
    slice = random.sample(article_list, 3)
    # max = Article.objects.aggregate(count=Count('id'))['count']
    # for i in range(num):
    #     article_list.append(Article.objects.get(id=random.randint(1, max)))
    return slice

@register.simple_tag
def get_all_type():
    return ArticleType.objects.all()


@register.simple_tag
def article_with_tag():
    return ArticleTag.objects.all()

@register.simple_tag
def get_all_article():
    return Article.objects.all().defer('content')

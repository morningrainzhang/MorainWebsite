from django.core.paginator import Paginator
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.text import slugify
from markdown import Markdown
from markdown.extensions.toc import TocExtension

from blog.models import *


# Create your views here.
def article_list(request):
    article_all_list = Article.objects.all()
    paginator = Paginator(article_all_list, 3)
    page_num = request.GET.get('page', 1)
    page_of_articles = paginator.get_page(page_num)
    content = {}
    content['page_of_articles'] = page_of_articles
    return render_to_response('blog/index.html', content)


def article_detail(request, article_pk):
    content = {}
    article = get_object_or_404(Article, pk=article_pk)

    # article.content = markdown(article.content,
    #                               extensions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ])
    md = Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        TocExtension(slugify=slugify),
    ], )
    article.content = md.convert(article.content)
    article.toc = md.toc
    content['article'] = article
    content['previous_article'] = Article.objects.filter(create_time__gt=article.create_time).last()
    content['next_article'] = Article.objects.filter(create_time__lt=article.create_time).first()
    return render_to_response('blog/elements.html', content)


def article_type_list(request, article_type_pk):
    content = {}
    article_type_list = Article.objects.filter(article_type_id=article_type_pk)
    paginator = Paginator(article_type_list, 4)
    page_num = request.GET.get('page', 1)
    page_of_articles = paginator.get_page(page_num)
    content['page_of_articles'] = page_of_articles
    # content['articletype'] = get_object_or_404(ArticleType, pk=article_type_pk)
    return render_to_response('blog/index.html', content)


def article_with_date(request):
    # months = Article.objects.dates('publish_time', 'month', order="DESC")
    return render_to_response('blog/timeline.html')

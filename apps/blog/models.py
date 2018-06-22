from django.db import models
from simditor.fields import RichTextField
from django.contrib.auth import get_user_model
from easy_thumbnails.fields import ThumbnailerImageField

User = get_user_model()


class ArticleType(models.Model):
    type_name = models.CharField(max_length=15, verbose_name='分类类型')
    type_describe = models.CharField(max_length=50, null=True, verbose_name='分类描述')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


class ArticleTag(models.Model):
    tag_name = models.CharField(max_length=15, verbose_name='标签名称')

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    describe = models.CharField(max_length=50, verbose_name='文章描述')
    # content = RichTextField(verbose_name='文章内容')
    content = models.TextField(verbose_name='文章内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后一次更新时间')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='作者')
    is_deleted = models.BooleanField(default=False, verbose_name='能否删除')
    article_image = ThumbnailerImageField(upload_to='image/article/', verbose_name='文章封面')

    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE, verbose_name='文章类型')
    tags = models.ManyToManyField(ArticleTag, blank=True)

    def __str__(self):
        return "<Artivle: %s>" % self.title

    class Meta:
        ordering = ['-create_time']
        verbose_name = '文章'
        verbose_name_plural = '文章'

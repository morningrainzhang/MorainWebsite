from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Novel(models.Model):
    """
    小说模型
    """
    title = models.CharField(max_length=100, verbose_name='小说标题', help_text="小说标题")
    state = models.CharField(max_length=20, null=True, verbose_name='小说状态', help_text="小说状态")
    author = models.CharField(max_length=50, verbose_name='小说作者', help_text="小说作者")
    type = models.CharField(max_length=20, default='未分类', verbose_name='小说类型', help_text="小说类型")
    count_word = models.IntegerField(null=True, verbose_name='小说字数', help_text="小说字数")
    abstract = models.CharField(max_length=500, verbose_name='小说简介', help_text="小说简介")
    novel_image = models.URLField(null=True, verbose_name='小说封面', help_text="小说封面")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', help_text="添加时间")
    novel_url = models.URLField(null=True, verbose_name='小说网址', help_text="小说网址")
    click_num = models.IntegerField(default=0, verbose_name="点击数", help_text="点击数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数", help_text="收藏数")

    class Meta:
        verbose_name = '小说'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Section(models.Model):
    """
    小说章节模型
    """
    title = models.CharField(max_length=50, verbose_name='章节标题')
    content = models.TextField(verbose_name='章节内容', null=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    num = models.IntegerField(null=True, verbose_name='章节顺序')
    section_url = models.URLField(null=True, verbose_name='章节网址')
    click_num = models.IntegerField(default=0, verbose_name="点击数", help_text="点击数")
    is_new = models.BooleanField(default=False, verbose_name="是否新增", help_text="是否新增")
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='小说', related_name='novel')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.title


class UserFav(models.Model):
    """
    用户收藏操作
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name="小说", help_text="小说id")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

        # 多个字段作为一个联合唯一索引
        unique_together = ("user", "novel")

    def __str__(self):
        return self.user.username

class UserReadRecord(models.Model):
    """
    用户阅读章节记录
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    novel = models.ForeignKey(Novel, on_delete=models.DO_NOTHING, verbose_name='小说',help_text="小说id")
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING, verbose_name='章节',help_text="章节id")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '用户阅读记录'
        verbose_name_plural = verbose_name
        ordering = ['-id']

        # 多个字段作为一个联合唯一索引
        # unique_together = ("user", "section")

    def __str__(self):
        return self.user.username


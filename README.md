# MorainWebsite
这是我想建立的一个网站，名字叫MorainWebsite。现已上线于(www.morainz.com)  
通过Ubuntu+Nginx+Uwsgi部署。  
基于流量1M小水管的腾讯云。  

## 为什么建立
源于对python的兴趣，Django框架的好奇。  
任何项目来源于需求，做一个个人网站的需求很简单，Just For Myself。  
做一个小网站，放自己感兴趣的内容，在偌大的互联网留下自己的一片小空间，也是很有意思也很有意义的事情。
## Content
想做的东西很多，需求皆来源于自己。

1. `blog`:首先我得有一个博客，这是程序员的标配。不同于github+hexo等可以随意换换主题的半自助博客，我需要美美的前端，靠得住的后台操作，以及充满干货的内容，最好可以admin后台编辑文章，顺便支持Markdown语法就更好了。
2. `gallery`:不能光用文章来填满生活，还要用美美的照片丰富一下。很多对摄影有兴趣的小伙伴并不满足于朋友圈的九图。除了发布到类似花瓣的平台，创建一个属于自己的相册就是很重要的需求了。毕竟既然没有能力办个人摄影展，上传到服务器占用一下云空间YY下自己也是可以的嘛。嗯，前端最好不要花里胡哨，抢占图片C位。简单，性冷淡，最好弄个瀑布流。因为是1M小水管，加载平均5M的原图估计要个小半天，要加个缩略图。
3. `library`:一个戒不掉的小习惯，看玄幻小说。除了完本，玄幻类的小说都需要等待连载，基本都是每天两章。无聊时候都是像刷微博一样刷着山寨小说网站，盼望着更新。不如自己建一个小说网站，按照自己喜欢的风格建立ui，用爬虫爬取自己喜欢的几部小说，应该不算太违规。服务器设置十分钟爬取一次，更新到个人网站，最好可以邮箱提醒我，让我告别刷刷刷。
4. `one`:火极一时的app-ONE一个。一天一条鸡汤，丰富伪韩粉的内心世界。安卓以及ios端UI简洁大气，但是web端就略显寒酸，不如按自己审美自己改一个，爬虫每日更新。

## Feature
* blog
	* DjangoUeditor（实现admin后台富文本编辑，支持markdown）
	* 本地上传markdown文件，以html格式保存
	* 代码显示highlight	
	* 文章目录（显示及跳转）
	* 标签页，分类选择，显示
	* 归档
	* 全局搜索（未完成）
* gallery
	* 瀑布流
	* 缩略图
* library
	* 用户登陆注册
	* 用户收藏小说
	* 小说自动更新（celery）
	* 小说更新邮箱提醒（django.core.mail）
	* DRF实现RESTAPI
	* xadmin后台管理
* one
	* 待开发

## Knowledge
通过项目进行编程学习是亘古不变的道理。通过项目去实践各种python包，django的第三方库，是行之有效的学习方式。项目知识点总结：


* `django2.0`
* `django.mail`
* `djangp.auth`
* `rest_framework`
* `rest_framework_jwt`
* `xadmin`
* `DjangoUeditor`
* `celery`
* `celery-beat`
* `mysql`
* `redis`

## 界面
### index
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/index.jpg)
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/index_blog.jpg)
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/index_gallery.jpg)
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/index_library.jpg)
### blog
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/blog1.jpg)
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/blog2.jpg)
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/blog3.jpg)
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/blog4.jpg)
### gallery
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/gallery1.jpg)
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/gallery2.jpg)
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/gallery3.jpg)
### novel
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/novel1.jpg)
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/novel2.jpg)
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/novel3.jpg)
#### SIGNIN/OUT
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/novel4.jpg)
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/novel5.jpg)
### function
#### xadmin
> 使用xadmin进行后台管理，并实现富文本编辑，其中支持markdown书写。

![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/xadmin%E5%90%8E%E5%8F%B0.jpg)
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/%E5%AF%8C%E6%96%87%E6%9C%AC%E7%BC%96%E8%BE%91.jpg)
#### 章节更新
>通过celery实行每10分钟定时爬取，爬取结果后通过获取signal，向用户进行邮件提醒。

![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/%E7%AB%A0%E8%8A%82%E6%9B%B4%E6%96%B0.png)
![](http://morain.oss-cn-hangzhou.aliyuncs.com/MorainWebsite/%E7%9F%AD%E4%BF%A1%E6%8F%90%E9%86%92.png)




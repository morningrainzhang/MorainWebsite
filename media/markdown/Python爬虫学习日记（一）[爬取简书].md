# Python爬虫学习日记（一）[爬取简书]
## 前言
之前在简书上发现一位关于Python爬虫大神，他从0学起Python爬虫。从开始的默默无闻的发文章，没有人关注没有人阅读也没有人点赞，然而......  
所以第一篇日志是向这位大神致敬，爬取他的文章再保存成pdf格式到本地再学习。  
[向右奔跑](http://www.jianshu.com/u/54b5900965ea)简书
## 1.发送requests获得服务器响应
###方式1:
```
urllib.request.urlopen(url).read().decode('utf-8')
```
### 方式2：
	request = urllib2.Request(url = url, headers = headers)
	response = urllib2.urlopen(request, timeout = 5)
	page = response.read().decode('utf-8')
### 方式3：
	requests.get(url).content.decode('utf-8')
	

##解析Response响应
```

```


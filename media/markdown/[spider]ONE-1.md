## 背景
曾经几时，[一个ONE](http://wufazhuce.com/) 席卷了各类青年的手机。  
这款APP    
每天发布的一句话，一张图  
它顺应这个快速且碎片化的时代，**快捷**，**简洁**  
不同于各种味道的鸡汤  
不同于质量参差不齐的散文  
在ONE中，你不用去选择，每天的推送无感或者不喜欢就关闭软件，打动到内心就充其量截屏发个票圈  
>在其中  
可能某个总结人生经验的一句话从而博得你的同感  
无论是亲情友情或是爱情  
可能在你某个失意时刻振奋你的生活  
更加的努力和热爱生活
当然也可能让你更加明白现实以及负能量 
![](https://ws3.sinaimg.cn/large/006tNc79gy1fjtti6qzjdj31kw11xu0z.jpg)


或许每一个现在手机中还有这个APP的同学，还有一个向往文艺的心。

## 网页介绍
![ONE一个](https://ws4.sinaimg.cn/large/006tNc79gy1fjtmhxovymj31bi1cqqv5.jpg)

这个网页简洁到略显简陋，明显快被时代所抛弃。

不过也难怪，网页版用户显然不是ONE的侧重方向。

当然，网页的UI设计和我们写爬虫没有什么关系。

## 网页分析

![](https://ws1.sinaimg.cn/large/006tNc79gy1fjtmyx3ny2j31kw0ye1ky.jpg)

用chorme分析网页，利用Elements左边的小箭头可以快速跳转到文字在网页源代码的位置。

对所需数据反复点击，即可对网页构造内容有所了解，有利于后面对页面的解析。

# 利用Requests与Bs4爬取网页
## 导入requests包

	import requests

如果没有包，利用pip下载到python即可。pip可以解决大多数python包的下载安装了。  

python2:

	pip install requests

本篇日记内容就是在python2环境下。
	
python3:

	pip install requests

## 获取页面：

~~~
url = "http://www.wufazhuce.com/"
page = requests.get(url).content
print page
~~~
![](https://ws2.sinaimg.cn/large/006tNc79gy1fjtmwhipr4j30n60aqdih.jpg)

这样获得的内容就打印在控制台上，发现我们所需的数据就在该页面中。

## 解析页面
~~~
from bs4 import BeautifulSoup

soup = BeautifulSoup(page, 'html.parser')

for i in soup.find_all('div',class_ = 'item'):
    onelist = i.find_all('a')
    image = onelist[0].img['src']
    word = onelist[1].text
    infolist = i.find_all('p')
    id = infolist[0].text
    date = infolist[1].text+' '+infolist[2].text
~~~

BeautifulSoup做的工作就是对html标签进行解释和分类，不同的解析器对相同html标签会做出不同解释。
第一个参数是获取的页面
第二个参数是解析器
解析器常用的有三个：

* html.parser
* lxml
* html5lib  

python内部默认的解析器"html.parser"，其自动补全标签的功能还有很差，但是应付这个简单的网页没有任何问题。而“lxml”的解析速度非常快，对错误也有一定的容性。
“html5lib”对错误的容忍度是最高的，而且一定能解析出合法的html5代码，但速度很慢。

根据对网页的具体分析，以上解析逻辑：

1. 搜索网页中class类型为‘item’的div，得到一个列表，其中一个元素就包括一天的数据信息。
2. 解析一天的数据，检索其中所有a标签，得到一个由a标签组成的列表，在第一个a标签中获得当天的图片url；第二个a标签获取当天的一句话。
3. 检索一天的p标签，其中第一个就是今天的id，而第二个标签就是年月日了。
4. 循环列表，获取七天的数据。

## 保存数据为dict格式
	list = []
	soup = BeautifulSoup(page, 'html.parser')
	for i in soup.find_all('div',class_ = 'item'):
	    onelist = i.find_all('a')
	    image = onelist[0].img['src']
	    word = onelist[1].text
	    infolist = i.find_all('p')
	    id = infolist[0].text
	    date = infolist[1].text+' '+infolist[2].text
	    data = {
	        'image':image,
	        'word':word,
	        'id':id,
	        'date':date
	    }
	    list.append(data)
	for dict in list:
		for key in dict:
	    	print key, '：', dict[key]
   ![](https://ws2.sinaimg.cn/large/006tNc79gy1fjts0mgemjj31e60m4dot.jpg)
   这样我们就获取了七天内ONE模块中各种数据，保存为dict格式，无论是存为Json格式应用于web数据，还是存储于mongoodb，都十分的方便。
   
# 学习总结
今天学到requests，beautifulsoup的简单应用，爬取无需登录的无反爬虫的静态网页。  
写到这一步，但就爬取ONE来说，其实还有很多爬取工作还未完成。


比如：  

1. [一个ONE](http://wufazhuce.com/)网页中ONE文章，ONE模块还未爬取。
2. 如何解决爬取过往数据，比如说一年内的数据，而不是网站上显示的7天。
3. 数据保存到本地数据库或云端。

**问题有待解决**



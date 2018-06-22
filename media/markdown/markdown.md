# Markdown简介

>Markdown 是一种轻量级的「标记语言」，它的优点很多，目前也被越来越多的写作爱好者，撰稿者广泛使用。看到这里请不要被「标记」、「语言」所迷惑，Markdown 的语法十分简单。常用的标记符号也不超过十个，这种相对于更为复杂的HTML 标记语言来说，Markdown 可谓是十分轻量的，学习成本也不需要太多，且一旦熟悉这种语法规则，会有一劳永逸的效果。
![dog](https://ws2.sinaimg.cn/large/006tNc79gy1fjllij94qvj31kw11x1l4.jpg)

# 为什么要用MarkDown
有一天，想随便写点什么，就点开各种操作按键，功能强大的*Word*，间接想起论文的复杂格式和痛苦，发觉短短的几句话就用`.doc .docx`来承载实在太过大材小用，而使用`.txt`又显得不够庄重，即使在`Win`里记事本是去格式神器。

刚好这几天搭建了Hexo博客，与大多数大型同性社交网路都支持Markdown，例如github，简书，coding.......

发现，在如今越来越标准化的互联网环境下，Markdown已经算是一套写作标准。在这几乎被MarkDown统治的环境下，掌握这一项技能是很重要的，无论是编程的coder，还是写作的writer。

# 工欲善其事，必先利其器
## 创作工具
既然下定了决心学这一门「标记语言」，就要选择一把好用的武器。在Mac平台相较Win有更多的选择，例如：

* [Typora](https://www.typora.io/)：如记事本一般简洁的操作，却可以书写标准MarkDown，犹如光头般清爽。

* [Bear](http://www.bear-writer.com/):图标好评，界面好评，操作好评，设备之间互联性满分，收费差评。

* [Macdown](http://macdown.uranusjr.com/):国产良心软件，免费开源，种草。

对比了很多编辑软件，最终我还是选择*Github*出品的*Atom*搭配插件*markdown preview*,享受充分的个性化以及实时显示。

重要的是！

适配*Window*!!!

参考教程：[Atom与markdown](http://www.jianshu.com/p/ad3e737e5dc2)

进入Atom后的操作快捷键：

windows : `ctrl + shift + m`

mac : `command + shift + m`

## 图床工具
互联网时代，单纯的文字显得干枯，图片显得极其重要。

为了证明文章目标不是刊登在知音读者，就需要插一张图。

![IMG_1395.jpg](https://i.loli.net/2017/09/15/59bbedbf0632f.jpg)

而选择恰当的图片又是区分专业论文和公众号搞笑推文的只要因素，所以要慎重。

那么如何让本地图片可以显示在每一台设备？那就需要上传到云端，再以链接的方式添加到*.md*文件中。

这种操作就需要使用云床，推荐：

*  [sm.ms](https://sm.ms/)：网页版*sm.ms*还有*app*版，可以将手机里的图片上传直接返回*.md*格式，很是方便。

*  [围脖图床修复计划](http://weibotuchuang.sinaapp.com/)：网页端插件 图片一拖即可。

*  [七牛](https://portal.qiniu.com/create)：开发者云储存 极其稳定 就是靠谱。

# 如何使用MarkDown？
## 标题
代码：

```
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```
效果：
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
## 链接
- 网页链接
    - 内联
        - 代码：`[百度](www.baidu.com)`
        - 效果：
        - 这是一个[百度](www.baidu.com)链接
    - 引用
        - 代码： `这是一个[百度][1]链接 + [1]:www.baidu.com`
        - 效果：
        - 这是一个[百度][1]链接 适合同一网址多处引用
   [1]: www.baidu.com/
- 图片链接
    - 本地
        - 代码：``![header](/Users/zhangchenyu/Downloads/IMG_1093.JPG)``
        - 效果：
        - ![header](/Users/zhangchenyu/Downloads/IMG_1093.JPG)
    - 内联
        - 代码：`![header](https://ws3.sinaimg.cn/large/006tNc79gy1fjkpdl2ny4j30hs0hsdha.jpg)`
        - 效果：
        - ![header](https://ws3.sinaimg.cn/large/006tNc79gy1fjkpdl2ny4j30hs0hsdha.jpg)

     但是，图片太大怎么办？
    - 修改图片大小
        - `<img src="https://ws3.sinaimg.cn/large/006tNc79gy1fjkpdl2ny4j30hs0hsdha.jpg" width="100" height="100">`
        - 效果：
        - <img src="https://ws3.sinaimg.cn/large/006tNc79gy1fjkpdl2ny4j30hs0hsdha.jpg" width="100" height="100">



## 强调
* 正常
* `*斜*`         *斜*
* `**粗**`      **粗**
* `***又粗又斜***`    ***又粗又斜***
* `~~划线~~` ~~划线~~
* `==下划线==` __划线__

## 分割线
***、___（3个星号、底线）   
华丽丽的分割线~

代码：`***`
***
代码：`___
___

## 列表
### 有序
代码：

    0. 打开冰箱门
    1. 把大象塞进去
    4. 关上冰箱门

效果：

1. 打开冰箱门
2. 关上冰箱门
4. 把大象塞进去

可以看出，有序列表的顺序与编号大小有关但是与内容无关。

### 无序
代码：

   ```
   * 打开冰箱门
   		* 把大象塞进去
   			* 关上冰箱门
   ```
效果：

* 打开冰箱门
    * 把大象塞进去
        * 关上冰箱门

无序列表可以根据`Tab`键调整，并且 `* + - `三个符号效果相同。

### 引用
代码：

    > 打开冰箱门
    >> 把大象塞进去
    >>> 关上冰箱门

效果：

> 打开冰箱门
>> 把大象塞进去
>>> 关上冰箱门

可见引用列表与`Tab`键无关，与`>`数量有关

## 代码区域
- `Tab`键缩进或连续空格
- `'`号或`~`对应一个一行代码 三个包括区域为代码区域

用python的头文件做示范

代码：

```
~~~
#-*- coding:utf-8 -*-
#! /usr/local/bin/python
import sys
reload(sys)
sys.setdefaultencoding('utf8')
~~~
```
效果：

~~~
#-*- coding:utf-8 -*-
#! /usr/local/bin/python
import sys
reload(sys)
sys.setdefaultencoding('utf8')
~~~

## 图表

代码：

	|第一列|第二列|第三列|
	----|------|----
	1 | 2  | 3
	1 | 2  | 3
	1 | 2  | 3
效果:

|第一列|第二列|第三列|
----|------|----
1 | 2  | 3
1 | 2  | 3
1 | 2  | 3

代码：

```
|第一列|第二列|第三列|
|:-:|:-|-:|
|第一列是居中的|第二列是居左的|第三列是居右的|
```

效果:

|第一列|第二列|第三列|
|:-:|:-|-:|
|第一列是居中的|第二列是居左的|第三列是居右的|


# 使用它，爱上它
无论  
写一封邮件  
写一篇博客  
还是写一篇公众号推文  
Markdown  
让文字与图片与其彼此融合

使用它  
并爱上它

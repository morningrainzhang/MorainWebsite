# Ubuntu+Nginx+Uwsgi部署Django

## 登录服务器
选用了阿里云Ubuntu系统盘
使用ssh在mac终端登录
`ssh root@120.78.183.192`

### 创建超级用户
useradd -m -s /bin/bash morain
usermod -a -G sudo morain
passwd morain
su - morain

###更新系统
```
# update是下载源里面的metadata（更新整个仓库的版本信息）
apt-get update
# upgrade是根据update命令下载的metadata决定要更新什么包（跟新软件包）
apt-get upgrade
```
### 修改默认pip以及python
阿里云自带python2.7以及3.5。为了顺应时代的潮流，我们只需要将`python`命令改为调用3.5即可。

```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150

#切换
sudo update-alternatives --config python
```
设置并更新pip

```
#下载pip3
apt-get install python3-pip
#删除pip快捷方式
rm /usr/bin/pip
#将pip3软连接给pip
ln -s /usr/bin/pip3 /usr/bin/pip
pip install --upgrade pip
```
运行`pip -V`即可发现我们的pip3更新到最新版本，且包地址为`/usr/local/lib/python3.5/dist-packages`

### 虚拟环境
安装virtualenv

```
pip3 install virtualenv
pip3 install virtualenvwrapper
```
配置virtualenvwrapper  
`vim /usr/local/bin/virtualenvwrapper.sh`  
将virtualenvwrapper加入环境变量  
`vim ~/.bashrc `
在最后添加

```
if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
    export WORKON_HOME=/root/virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
fi
```
重新载入配置文件
`source .bashrc`  
 
| 功能  |  使用方法  |
| :----:| :----: |
| 创建基本环境  |   mkvirtualenv [环境名]    |
| 删除环境   |   rmvirtualenv [环境名]    |
| 激活环境 |   workon [环境名]    |
| 退出环境  |   deactivate    |
| 列出所有环境 |   workon 或者 lsvirtualenv -b  |

`mkvirtualenv django2.0`

## 安装Mysql
	sudo apt-get install mysql-server
	
	sudo apt-get install mysql-client
	
	sudo mysql_secure_installation
检查是否安装成功

`sudo netstat -tap | grep mysql`

### 修改mysql配置文件
`vim /etc/mysql/mysql.conf.d/mysqld.cnf`

* `max_allowed_packet      = 256M`
* `interactive_timeout     = 2880000`
* `wait_timeout            =2880000`

`service mysql restart`

**更改远程访问**

`#bind-address= 127.0.0.1`

**重启**

`service mysql restart`


**登录mysql,设置root权限**

`mysql -uroot -p 
`

```
grant all privileges on *.* to root@"%" identified by "hz123456" with grant option;
flush privileges;
exit;
```
**mysql的log地址**

`/var/log/mysql/error.log`

**mysql使用方法**  
`service mysql restart ||sudo /etc/init.d/mysql restart/start/stop`



## 安装Redis
功能：

1. 缓存常用数据，以提升加载速度。
2. 作为celery任务队列的储存数据库。

```
cd /root
tar zxvf /root/redis-4.0.9.tar.gz

make
make install
make test

mkdir  /usr/local/redis
mkdir  /usr/local/redis/bin
mkdir  /usr/local/redis/etc
mkdir  /usr/local/redis/db

cp /usr/local/bin /root/redis-4.0.9
cp /usr/local/redis4.0.8/src/mkreleasehdr.sh /usr/local/redis/mkreleasehdr.sh
cp /usr/local/redis-4.0.8/redis.conf /usr/local/redis/etc 
vim /usr/local/redis/etc/redis.conf
vim /usr/local/redis/log-redis.log
```

`apt-get install redis-server`
### 项目管理
本地运行

`pip freeze > requirements.txt`

将本地项目上传至**/var/www/**

```
cd /var/www/morain
pip install -r requirements.txt
```

安装mysqlclient报错

`Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-qcrdym68/mysqlclient/`

解决方式：

`apt-get install libmysqlclient-dev python3-dev`

### django基本配置
python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic

python manage.py createsupreruser

sudo pip install uwsgi

vim /etc/nginx/sites-enabled/default

## 安装文件
### nginx

sudo apt install nginx

vim /etc/nginx/sites-enabled/default

/etc/init.d/nginx start (restart / stop)# 分别为nginx启动、重启和停止


`vim /etc/nginx/sites-enabled/default`

```
upstream django{
		server 127.0.0.1:8001;
	}

server {
    listen      80;
    server_name www.morain.com;
    charset     utf-8;
 
    client_max_body_size 75M;
 
    location /media  {
        alias /var/www/morain/media;
    }
 
    location /static {
        alias /var/www/morain/static;
    }
 
    location / {
        uwsgi_pass  django;
        include     uwsgi_params;
    }
}

```
### uwsgi
apt-get install uwsgi  

vim /var/www/uwsgi.ini  

uwsgi --ini /var/www/uwsgi.ini


```
[uwsgi]
project = morain
# 项目目录,该目录为settings.py所在的目录
chdir=/var/www/morain
# 指定项目的application,该目录为wsgi.py所在的目录
module=morain.wsgi
# 指定sock的文件路径
socket=:8001
# 启用主进程
master=true
# 进程个数
workers=5
# 自动移除unix Socket和pid文件当服务停止的时候
vacuum=true
# 序列化接受的内容，如果可能的话
thunder-lock=true
# 启用线程
enable-threads=true
# 设置自中断时间
harakiri=30
# 设置缓冲
post-buffering=4096
# 是否自动重启服务器, 例如项目某文件有变换直接重启服务器
py-autoreload = 1
# 设置日志输出目录
daemonize = /var/log/uwsgi/uwsgi.log

```

### supervisor

`vim /etc/supervisor/conf.d/celery.conf`

```
[program:celery-queue-fetch]
;程序要执行的命令, -Q 指定了生成和接受任务的队列,多个用都好分开 -c为workr的数量,原意为并发数量
command=/root/virtualenvs/django2.0/bin/python3 /var/www/morain/manage.py celery worker --loglevel=info
;程序执行时候所在目录
directory=/var/www/morain/
;执行程序使用的用户
user=root
;启动的程序的实例数,默认是1
numprocs=1
stdout_logfile=/var/www/morain/logs/celery/celery.log
stderr_logfile=/var/www/morain/logs/celery/celery.log
;在启动supervisor时候自动启动
autostart=true
;当程序可能因为某些原因没有启动成功会自动重启
autorestart=true
;启动的等待时候,我想是为了重启能杀掉原来进程预留的时间
startsecs=10
;进程发送停止信号等待os返回SIGCHILD的时间
stopwaitsecs=10
;低优先级的会首先启动最后关闭
priority=998
;以下2句是为了保证杀掉进程和其子进程而不会只杀死其控制的程序主进程而留下子进程变为孤立进程的问题
stopsignal=KILL
stopasgroup=true


[program:celerybeat]
command=/root/virtualenvs/django2.0/bin/python3 /var/www/morain/manage.py celery beat --loglevel=DEBUG
directory=/var/www/morain/
user=root
numprocs=1
stdout_logfile=/var/www/morain/logs/celery/celery_beat.log
stderr_logfile=/var/www/morain/logs/celery/celery_beat.log
autostart=true
autorestart=true
startsecs=10
priority=999
stopsignal=KILL
stopasgroup=true

```

`supervisorctl start|restart|stop all|name`

## 日志管理
###celery
`tail -f /var/www/morain/logs/celery/celery.log`
`tail -f /var/www/morain/logs/celery/celery_beat.log`
###uwsgi
`tail -f /var/log/uwsgi.log`
`tail -f /var/log/uwsgi/uwsgi.log`
###redis
`tail -f /var/log/redis/redis-server.log`
###nginx
`tail -f /var/log/nginx/error.log`
`tail -f /var/log/nginx/access.log`
###django
`tail -f /var/www/morain/logs/morain.log`


## 进程管理
### 查看进程
```
ps -ef | grep uwsgi
ps -ef | grep nginx
killall -9 uwsgi
killall -9 nginx
/etc/init.d/nginx restart 
`uwsgi --ini /var/www/uwsgi.ini`
```
###supervisor
`supervisorctl start|restart|stop all|name`
`supervisorctl shutdown`

## Ubuntu常用代码
服务器信息：vim /etc/hosts
netstat -nltp
reboot 重启服务器
```
uwsgi -x /home/ubuntu/wx/uwsgi.xml
tail -f /home/ubuntu/wx/wechat.log
tail -f /var/log/uwsgi.log
vim /var/log/nginx/access.log
vim /var/log/nginx/error.log
```




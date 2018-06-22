server {   # 这个server标识我要配置了
        listen 80;  # 80 是http默认的端口， 443 是https默认的端口（网页一般使用这两个端口）
        server_name www.morainz.com ;  # 你访问的路径前面的url名称
        access_log  /var/www/html/MorainWebsite/log/access.log;  # Nginx日志配置
        error_log  /var/www/html/MorainWebsite/log/error.log;    # Nginx错误日志配置
        charset  utf-8; # Nginx编码
        gzip on;  # 启用压缩,这个的作用就是给用户一个网页,比如3M压缩后1M这样传输速度就会提高很多
        gzip_types text/plain application/x-javascript text/css text/javascript application/x-httpd-php application/json text/json image/jpeg image/gif image/png application/octet-stream;  # 支持压缩的类型

        error_page  404           /404.html;  # 错误页面
        error_page   500 502 503 504  /50x.html;  # 错误页面

        # 指定项目路径uwsgi
        location / {        # 这个location就和咱们Django的url(r'^admin/', admin.site.urls),
            include uwsgi_params;  # 导入一个Nginx模块他是用来和uWSGI进行通讯的
            uwsgi_connect_timeout 30;  # 设置连接uWSGI超时时间
            # 指定uwsgi的sock文件所有动态请求就会直接丢给他
            uwsgi_pass unix:/var/www/html/MorainWebsite/script/uwsgi.sock;
        }

        # 指定静态文件路径
        location /static/ {
            alias /var/www/html/MorainWebsite/static;
        }
        
        location /media/ {
            alias /var/www/html/MorainWebsite/media;
        }
    }
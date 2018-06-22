# encoding: utf-8

from rest_framework import permissions

"""
在utils中新建permissions，这是我们自定义的permissions，然后粘贴上面的IsOwnerOrReadOnly
这个自定义的permission类继承了我们的BasePermission。它有一个方法叫做has_object_permission，是否有对象权限。
会检测我们从数据库中拿出来的obj的owner是否等于request.user
这个obj是我们数据库中的表，所以这里的owner应该改为我们数据库中的外键user
安全的方法也就是不会对数据库进行变动的方法，总是可以让大家都有权限访问到。
"""


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
  只允许作者修改但允许所有人读的权限设置
    """

    def has_object_permission(self, request, view, obj):
        # 所有用户都允许读取,所以安全的http方法会直接放行
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True

        # 写入权限需要作者本人
        return obj.user == request.user

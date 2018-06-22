"""MorainWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

import xadmin
from MorainWebsite.settings import MEDIA_ROOT
from MorainWebsite.views import index
from library.apiviews import NovelListViewSet, SectionListViewSet, UserFavViewset
from library.view import UsersView, NovelsView, SectionsView, DetailView, novel_fav, novel_update, BookrackView, \
    users_logout
from rest_framework.authtoken import views
# from goods.views import GoodsListView,
# from goods.views_base import GoodsListView
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from users.apiviews import EmailCodeViewset, UserViewset

router = DefaultRouter()
router.register(r'code', EmailCodeViewset, base_name="code")
router.register(r'users', UserViewset, base_name="users")
router.register(r'novels', NovelListViewSet, base_name="novels")
router.register(r'sections', SectionListViewSet, base_name="sections")
# 配置用户收藏的url
router.register(r'userfavs', UserFavViewset, base_name="userfavs")
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    # jwt的token认证
    path('api-jwt-token/', obtain_jwt_token),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('users/', UsersView.as_view(), name='users'),
    path('novels/', NovelsView.as_view(), name='novels'),
    path('sections/<int:novel_pk>/', SectionsView.as_view(), name='sections'),
    path('detail/<int:section_pk>/', DetailView.as_view(), name='detail'),
    path('update/', novel_update, name='update'),
    path('userfavs/<int:novel_pk>/', novel_fav, name='userfavs'),
    path('bookrack/', BookrackView.as_view(), name='bookrack'),
    path('logout/', users_logout, name='logout'),
    # path('novel/', TemplateView.as_view(template_name='novel/index.html'), name='index'),
    # path('novel/', TemplateView.as_view(template_name='novel/book_preview.html'), name='book_preview')
    path('simditor/', include('simditor.urls')),
    path('', index, name='home'),
    path('blog/', include('blog.urls')),
    path('gallery/', include('gallery.urls')),
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
]

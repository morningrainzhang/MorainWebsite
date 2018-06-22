from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
# Create your views here.

from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework_extensions.cache.mixins import CacheResponseMixin
# 设置登录与未登录限速
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from library.models import Novel, Section, UserFav
from library.serializers import UserFavSerializer, UserFavDetailSerializer, NovelSerializer, SectionSerializer
from library.filters import NovelFilter
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

# 小说列表分页类
class NovelsPagination(PageNumberPagination):
    page_size = 8
    # 向后台要多少条
    page_size_query_param = 'page_size'
    # 定制多少页的参数
    page_query_param = "page"
    max_page_size = 100


# 章节列表分页类
class SectionsPagination(PageNumberPagination):
    page_size = 12
    # 向后台要多少条
    page_size_query_param = 'page_size'
    # 定制多少页的参数
    page_query_param = "page"
    max_page_size = 100


class NovelListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    小说列表页，分页，搜索，过滤，排序,取某一个具体小说的详情
    """

    # queryset是一个属性
    # good_viewset.queryset就可以访问到
    # 函数就必须调用good_viewset.get_queryset()函数
    # 如果有了下面的get_queryset。那么上面的这个就不需要了。
    # queryset = Goods.objects.all()

    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    serializer_class = NovelSerializer
    pagination_class = NovelsPagination
    queryset = Novel.objects.all()

    # 设置列表页的单独auth认证也就是不认证
    authentication_classes = (TokenAuthentication,)

    # 设置三大常用过滤器之DjangoFilterBackend, SearchFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 设置排序
    ordering_fields = ('add_time', 'click_num', 'fav_num')
    # 设置filter的类为我们自定义的类
    # filter_class = NovelFilter
    filter_fields = ('title', 'author')

    # 设置我们的search字段
    search_fields = ('title', 'author')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class SectionListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    章节列表页，分页，搜索，过滤，排序,取某一个具体小说的章节列表
    """

    # queryset是一个属性
    # good_viewset.queryset就可以访问到
    # 函数就必须调用good_viewset.get_queryset()函数
    # 如果有了下面的get_queryset。那么上面的这个就不需要了。
    # queryset = Goods.objects.all()

    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    serializer_class = SectionSerializer
    pagination_class = SectionsPagination
    queryset = Section.objects.all()

    # 设置列表页的单独auth认证也就是不认证
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    # 设置三大常用过滤器之DjangoFilterBackend, SearchFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 设置排序
    ordering_fields = ('num', 'click_num')
    # 设置filter的类为我们自定义的类
    # filter_class = NovelsFilter

    # 设置我们的search字段
    search_fields = ('novel', 'title')

    filter_fields = ('novel', 'title')

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserFavViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    """
    list:
        获取用户收藏列表
    retrieve:
        判断小说是否已经收藏
    create:
        收藏小说
    """
    # queryset = UserFav.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = UserFavSerializer
    lookup_field = 'novel_id'
    # lookup_field = 'goods'
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    # 收藏数+1
    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     # 通过这个instance Userfav找到goods
    #     goods = instance.goods
    #     goods.fav_num +=1
    #     goods.save()

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    # 设置动态的Serializer
    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer

        return UserFavSerializer

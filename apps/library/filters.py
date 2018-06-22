#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: ??
@author: Morain
@file: filters.py
@time: 2018/5/17 04:01
"""
from django_filters import rest_framework as filters
from library.models import Novel


class NovelFilter(filters.FilterSet):
    """
    小说的过滤类
    """
    # 指定字段以及字段上的行为，在shop_price上大于等于
    title = filters.CharFilter(name="title", lookup_expr="icontains")
    author = filters.CharFilter(name="author", lookup_expr="icontains")

    class Meta:
        model = Novel
        fields = ['title', 'author']

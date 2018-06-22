#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from blog import views

urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('<int:article_pk>/', views.article_detail, name="article_detail"),
    path('type/<int:article_type_pk>', views.article_type_list, name="article_type_list"),
    path('date/', views.article_with_date, name="article_with_date"),
]

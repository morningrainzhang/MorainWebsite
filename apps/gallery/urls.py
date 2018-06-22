#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from gallery import views

urlpatterns = [path('', views.images_list, name="images_list"),
               path('about/', views.about, name="about"),
               path('contact/', views.contact, name="contact"),
               path('type/<int:image_type_pk>', views.image_type_list, name="image_type_list"),
               ]

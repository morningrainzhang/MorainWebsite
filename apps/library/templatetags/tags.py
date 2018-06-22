import random

from django import template

from library.models import *
from django.contrib.auth import get_user_model

User = get_user_model()
register = template.Library()


@register.simple_tag
def get_random_novel(num=4):
    return random.choices(Novel.objects.all(), k=num)


@register.simple_tag
def get_previous_section(novel):
    return Section.objects.filter(novel=novel)[:5]


@register.simple_tag
def get_last_section(novel):
    return Section.objects.filter(novel=novel).order_by('-add_time')[:5]


@register.simple_tag
def get_record_read_now(user):
    if User.objects.filter(username=user):
        return UserReadRecord.objects.filter(user=user).order_by("add_time").last()
    else:
        return None

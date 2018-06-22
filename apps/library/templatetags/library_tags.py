import random

from django import template

from library.models import *

register = template.Library()


@register.simple_tag
def get_recent_novel(num=4):
    return Novel.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def get_random_novel(num=4):
    return random.choices(Novel.objects.all(), k=num)


@register.simple_tag
def get_all_novel():
    return Novel.objects.all()


@register.simple_tag
def get_previous_section(novel):
    return Section.objects.filter(novel=novel)[:5]


@register.simple_tag
def get_last_section(novel):
    return Section.objects.filter(novel=novel).order_by('-num')[:5]


@register.simple_tag
def get_section_read_now(user):
    return UserFav.objects.filter(user=user).order_by("date_read").last()

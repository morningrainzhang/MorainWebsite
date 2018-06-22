# Generated by Django 2.0.5 on 2018-05-19 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20180517_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='click_num',
            field=models.IntegerField(default=0, help_text='点击数', verbose_name='点击数'),
        ),
        migrations.AddField(
            model_name='novel',
            name='fav_num',
            field=models.IntegerField(default=0, help_text='收藏数', verbose_name='收藏数'),
        ),
        migrations.AddField(
            model_name='section',
            name='click_num',
            field=models.IntegerField(default=0, help_text='点击数', verbose_name='点击数'),
        ),
    ]
# Generated by Django 2.0.5 on 2018-06-20 23:28

from django.db import migrations
import simditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180620_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=simditor.fields.RichTextField(verbose_name='文章内容'),
        ),
    ]
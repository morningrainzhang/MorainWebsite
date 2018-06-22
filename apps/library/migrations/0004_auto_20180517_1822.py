# Generated by Django 2.0.5 on 2018-05-17 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20180514_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novel',
            name='count_word',
            field=models.IntegerField(help_text='小说字数', null=True, verbose_name='小说字数'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='novel_image',
            field=models.URLField(help_text='小说封面', null=True, verbose_name='小说封面'),
        ),
    ]
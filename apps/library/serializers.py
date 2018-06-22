import re
from datetime import datetime, timedelta
from rest_framework import serializers
from library.models import Novel, Section, UserFav
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.validators import UniqueValidator


# User = get_user_model()


class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        fields = '__all__'
        # read_only_fields = []#不让前端修改

    # def get_section_list(self, obj):
    #     return obj.section


class SectionSerializer(serializers.ModelSerializer):
    novel = NovelSerializer(read_only=True)  # 外键显示信息

    class Meta:
        model = Section
        fields = '__all__'


# class DetailSectionSerializer(serializers.ModelSerializer):
#     novel = NovelSerializer(read_only=True)  # 外键显示信息
#
#     class Meta:
#         model = Section
#         fields = '__all__'

class UserFavDetailSerializer(serializers.ModelSerializer):
    # 通过novel_id拿到商品信息。就需要嵌套的Serializer
    novel = NovelSerializer()

    class Meta:
        model = UserFav
        fields = ("novel", "id")


class UserFavSerializer(serializers.ModelSerializer):
    # 表示当前用户的默认类
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav

        # 使用validate方式实现唯一联合
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'novel'),
                message="已经收藏"
            )
        ]

        fields = ("user", "novel", "id")

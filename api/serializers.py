from rest_framework import serializers
from blog.models import *

class SingleArticleSerializer(serializers.Serializer):
    title=serializers.CharField(required=True,max_length=128,allow_blank=False, allow_null=False)
    avatar=serializers.CharField(required=True,max_length=256,allow_blank=False, allow_null=False)
    content=serializers.CharField(required=True,max_length=2048,allow_blank=False, allow_null=False)
    created_at=serializers.DateTimeField(required=True, allow_null=False)

class SumbitArticleSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=128,allow_null=False,allow_blank=False,required=True)
    avatar=serializers.FileField(allow_null=False,allow_empty_file=False,required=True)
    content=serializers.CharField(max_length=2048,allow_null=False,allow_blank=False,required=True)
    category_id=serializers.IntegerField(required=True,allow_null=False)
    author_id=serializers.IntegerField(required=True,allow_null=False)
    is_slider=serializers.BooleanField(required=True,allow_null=False)
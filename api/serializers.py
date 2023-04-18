from rest_framework import serializers
from blog.models import *

class SingleArticleSerializer(serializers.Serializer):
    title=serializers.CharField(required=True,max_length=128,allow_blank=False, allow_null=False)
    avatar=serializers.CharField(required=True,max_length=256,allow_blank=False, allow_null=False)
    content=serializers.CharField(required=True,max_length=2048,allow_blank=False, allow_null=False)
    created_at=serializers.DateTimeField(required=True, allow_null=False)
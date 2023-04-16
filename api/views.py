from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.models import Article
# Create your views here.

class AllArticles(APIView):
    def get(self,request,format=None):
        try:
            all_articles=Article.objects.all().order_by('-created_at')[:10]
            data=[]
            for article in all_articles:
                data.append({
                    'title':article.title,
                    'cover':article.avatar.url if article.avatar else None,
                    'content':article.content,
                    'created_at':article.created_at,
                    'category':article.category.title,
                    'author':article.author.user.username,
                    'is_slider':article.is_slider,
                })
            return Response({'data':data},status=status.HTTP_200_OK)
        except:
            return Response({'status':'Internal Server Error!! try again later'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
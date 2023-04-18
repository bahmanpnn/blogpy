from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.models import Article
from .serializers import SingleArticleSerializer
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

        
class SingleArticle(APIView):
    def get(self,request,format=None):
        try:
            article_title=request.GET['article_title']
            target_articles=Article.objects.filter(title__icontains=article_title)

            # after finding articles with title searching now we must change data to json and dictionary like all articles
            # we can do like all articles and use loop and add every data in one dictionary of one list or
            # use serializer to do this action with drf library and packages!!
            # query-->object-->json -->return
            serialized_data=SingleArticleSerializer(target_articles,many=True)
            data=serialized_data.data
            
            return Response({'data':data},status=status.HTTP_200_OK)

        except:
            return Response({'status':'Internal Server Error!! try again later'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class FindArticle(APIView):
#     def get(self,request,article_title,format=None):
#         try:
#             article_title=request.GET.get[article_title]
#             target_articles=Article.objects.filter(title__icontains=article_title)

#             # after finding articles with title searching now we must change data to json and dictionary like all articles
#             # we can do like all articles and use loop and add every data in one dictionary of one list or
#             # use serializer to do this action with drf library and packages!!
#             # query-->object-->json -->return
            
#             serialized_data=SingleArticleSerializer(target_articles,many=True)
#             data=serialized_data.data
            
#             return Response({'data':data},status=status.HTTP_200_OK)

#         except:
#             return Response({'status':'Internal Server Error!! try again later'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SearchArticle(APIView):
    def get(self,request,format=None):
        try:
            from django.db.models import Q
            query=request.GET['query']
            articles=Article.objects.filter(Q(content__icontains=query))
            data=[]
            for article in articles:
                data.append({
                    'title':article.title,
                    'avatar':article.avatar.url if article.avatar else None,
                    'content':article.content,
                    'created_at':article.created_at.date(),
                    'category':article.category.title,
                    'author':article.author.user.username,
                    'is_slider':article.is_slider,
                })
            
            return Response({'data':data},status=status.HTTP_200_OK)

        except:
            return Response({'status':'Internal Server Error!! try again later'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

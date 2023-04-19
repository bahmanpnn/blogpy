from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.models import *
from .serializers import SingleArticleSerializer,SumbitArticleSerializer,UpdateArticleSerializer
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

#it has problem
class SubmitArticleView(APIView):
    def post(self,request,format=None):
        try:
            serializer=SumbitArticleSerializer(data=request.data)
            if serializer.is_valid():
                title=request.data.get['title']
                avatar=request.FILES['avatar']
                content=request.data.get['content']
                category_id=request.data.get['category_id']
                author_id=request.data.get['author_id']
                is_slider=request.data.get['is_slider']
            else:
                return Response({'status':'Bad Request!!'},status=status.HTTP_400_BAD_REQUEST)

            user=User.objects.get(id=auhtor_id)
            author=UserProfile.objects.get(user=user)
            category=ArticleCategory.objects.get(id=category_id)
            
            # new_article=Article(title=title,avatar=avatar,content=content,category=category,author=author,is_slider=is_slider)
            
            new_article=Article()
            new_article.title=title
            new_article.avatar=avatar
            new_article.content=content
            new_article.category=category
            new_article.author=author
            new_article.is_slider=is_slider
            
            new_article.save()

            return Response({'status':'article created'},status=status.HTTP_201_CREATED)
        except:
            return Response({'status':'Internal Server Error!! try again later'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateArticleView(APIView):
    def post(self,request,format=None):
        try:
            serializer=UpdateArticleSerializer(data=request.data)
            if serializer.is_valid():
                article_id=request.data.get['article_id']
                avatar=request.FILES['avatar']
            else:
                return Response({'status':'Bad Request!!'},status=status.HTTP_400_BAD_REQUEST)
            
            Article.objects.filter(id=article_id).update(avatar=avatar)
            return Response({'data':data},status=status.HTTP_200_OK)
        except:
            return Response({'status':'Internal Server Error!! try again later'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

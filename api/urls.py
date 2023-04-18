from django.urls import path
from . import views

urlpatterns=[
    path('articles/all/',views.AllArticles.as_view(),name='all-articles'),
    path('articles/',views.SingleArticle.as_view(),name='single-article'),
    # path('articles/find_article/<str:article_title>/',views.FindArticle.as_view(),name='find-article'),
    path('articles/search_article/',views.SearchArticle.as_view(),name='search-article'),
]
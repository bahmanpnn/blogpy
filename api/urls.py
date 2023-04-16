from django.urls import path
from . import views

urlpatterns=[
    path('articles/all/',views.AllArticles.as_view(),name='all-articles'),
]
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.

class IndexPageView(TemplateView):
    def get(self,request,**kwargs):
        articles=[]
        articles_query=Article.objects.all().order_by('-created_at')[:12]
        for article in articles_query:
            articles.append({
                'title':article.title,
                'avatar':article.avatar.url,
                'created_at':article.created_at.date(),
                'category':article.category.title
            })
        context={
            'articles':articles
        }
        return render(request,'blog/index.html',context)

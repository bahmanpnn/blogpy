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

        all_sliders=Article.objects.filter(is_slider=True)
        sliders=[]
        for slider in all_sliders:
            sliders.append({
                'category':slider.category.title,
                'title':slider.title,
                'author':slider.author.user.username,
                'author_avatar':slider.author.avatar.url if article.author.avatar else None,
                'slider_cover':slider.avatar.url if article.author.avatar else None,
                'created_at':slider.created_at.date(),
            })
            
        context={
            'articles':articles,
            'sliders':sliders,
        }
        return render(request,'blog/index.html',context)


class ContactPageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request,'blog/page-contact.html')

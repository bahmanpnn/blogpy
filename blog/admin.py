from django.contrib import admin
from .models import *
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user','avatar','about_user']

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display=['title','cover']

class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','category','created_at']
    search_fields=['title','content']


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleCategory,ArticleCategoryAdmin)

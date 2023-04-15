from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# from datetime import datetime
# Create your models here.

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext=os.path.splitext(value.name)[1]
    valid_extensions=['.jpg','.png','.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValiditionError('Unsupported file extension!!')

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    avatar=models.FileField(upload_to='files/user_avatars/',null=False,blank=False,validators=[validate_file_extension])
    about_user=models.CharField(max_length=512,null=False,blank=False)

    class Meta:
        verbose_name = "user_profile"
        verbose_name_plural = "user_profiles"

    def __str__(self):
        return self.user.username

class Article(models.Model):
    title=models.CharField(max_length=120,null=False,blank=False)
    avatar=models.FileField(upload_to='files/article_covers/',null=False,blank=False,validators=[validate_file_extension])
    content=RichTextField()
    created_at=models.DateTimeField(auto_now_add=True)
    # created_at=models.DateTimeField(default=datetime.now())
    # updated_at=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey("ArticleCategory", on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)


    class Meta:
        verbose_name = "article_cover"
        verbose_name_plural = "article_covers"

    def __str__(self):
        return self.title

class ArticleCategory(models.Model):
    title=models.CharField(max_length=120,null=False,blank=False)
    cover=models.FileField(upload_to='files/category_covers/',null=False,blank=False,validators=[validate_file_extension])

    class Meta:
        verbose_name = "category_cover"
        verbose_name_plural = "category_covers"

    def __str__(self):
        return self.title
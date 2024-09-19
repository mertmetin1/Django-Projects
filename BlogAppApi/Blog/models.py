#Blog/models.py

from django.db import models
from User.models import Blogger

# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.name


class Blog(models.Model):
    blog_owner=models.ForeignKey(Blogger,on_delete=models.CASCADE,related_name="blogModel")
    blog_title=models.CharField(max_length=200,blank=False,null=False, unique=True)
    blog_summary=models.TextField(blank=False,null=False)
    blog_context=models.TextField(blank=False,null=False)
    blog_category = models.TextField(blank=False,null=False)  #jsonfield veya yeni model kullanılabilir
    blog_is_active =models.BooleanField(default=True)
    blog_isGenByAi=models.BooleanField(default=False)
    blog_keywords=models.TextField(blank=False,null=False)
    
    blog_IsDeleted=models.BooleanField(default=False)
    
    blog_created = models.DateTimeField(auto_now_add=True)
    blog_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='Blogs'

    def __str__(self):
        return str(self.blog_title)
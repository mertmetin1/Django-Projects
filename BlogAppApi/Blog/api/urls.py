#Blog/api/urls.py
from django.urls import path
from Blog.api.views import BlogViewSet

# Instantiate your viewset
blog_viewset = BlogViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy',
    'retrieve': 'retrieve'
})

urlpatterns = [
    path('blogs/', blog_viewset, name='blog-list'),       # For listing and creating blogs
    path('blogs/<int:pk>/', blog_viewset, name='blog-detail')  # For retrieving, updating, and deleting a specific blog
]

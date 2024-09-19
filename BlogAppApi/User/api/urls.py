#User/api/urls.py


from django.urls import path
from User.api.views import BloggerViewSet

# Instantiate your viewset
blogger_viewset = BloggerViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy',
    'retrieve': 'retrieve'
})

urlpatterns = [
    path('bloggers/', blogger_viewset, name='blogger-list'),       # For listing and creating bloggers
    path('bloggers/<int:pk>/', blogger_viewset, name='blogger-detail')  # For retrieving, updating, and deleting a specific blogger
]

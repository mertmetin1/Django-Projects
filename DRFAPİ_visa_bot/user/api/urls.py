from django.urls import path
from user.api import views as api_views

#Class basedd viewler için oluşturulan urller


urlpatterns = [
    path('user/',api_views.User_filter.as_view(),name="user-settings"),
    path('user/<int:id>',api_views.User_Detail.as_view(),name="user-detail-id"),
  
]
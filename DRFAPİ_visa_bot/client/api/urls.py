from django.urls import path
from client.api import views as api_views

#Class basedd viewler için oluşturulan urller


urlpatterns = [
    path('client/',api_views.Client_filter.as_view(),name="client-settings"),
    path('client/<int:id>',api_views.Client_Detail.as_view(),name="client-detail-id"),
  
]
from django.urls import path
from bot_settings.api import views as api_views

#Class basedd viewler için oluşturulan urller


urlpatterns = [
    path('bot_settings/',api_views.Bot_Setting_filter.as_view(),name="bot-settings"),
    path('bot_settings/<int:id>',api_views.Bot_Setting_Detail.as_view(),name="bot-settings-detail-id"),
  
]



#fonskiyon tabanlı mthod ile requstleri karşılamak için oluşturulan urller
"""
urlpatterns = [
    path('bot_settings/',api_views.Bot_Setting_Filter,name="bot-settings"),
    path('bot_settings/<int:id>',api_views.Bot_Setting_Detail,name="bot-settings-detail-id"),
  
]

"""
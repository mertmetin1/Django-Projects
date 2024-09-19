from django.urls import path, include
from rest_framework.routers import DefaultRouter
from client.api.views import ClientViewSet,RegisterClientViewSet,LoginClientViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'client/register', RegisterClientViewSet, basename='register')
router.register(r'client/login',LoginClientViewSet,basename='login')

urlpatterns = [
    path('', include(router.urls)),  # Ensure the router is included correctly
]

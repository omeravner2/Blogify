from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountView
import django.contrib.auth.urls
router = DefaultRouter()
router.register(r'user', AccountView)


urlpatterns = [
    path('api/', include(router.urls)),


]

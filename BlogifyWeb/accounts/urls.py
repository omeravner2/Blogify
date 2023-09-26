from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountView

router = DefaultRouter()
router.register(r'user', AccountView)


urlpatterns = [
    path('api/', include(router.urls)),


]

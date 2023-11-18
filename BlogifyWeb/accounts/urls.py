from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountView, register_view, login_view, logout_view

router = DefaultRouter()
router.register(r'user', AccountView)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register', register_view, name='register_api'),
    path('api/login', login_view, name='login_api'),
    path('api/logout', logout_view, name='logout_api'),


]

from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', views.PostView)
router.register(r'comment', views.CommentView)
router.register(r'profile', views.ProfileView)


urlpatterns = [
    path('api/', include(router.urls)),


]
""" path('', views.HomePageView.as_view(), name="homepage"),
   path('like/<int:pk>', views.likeview, name="like-post"),
   path('profile/<int:pk>', views.ProfileView name="profile-details"),
   path('post/<slug:slug>/comment', views.CreateCommentView.as_view(), name="create-comment")"""
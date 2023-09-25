from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name="homepage"),
    path('post/<slug:slug>', views.PostView.as_view(), name="post-details"),
    path('create_post/', views.CreatePost.as_view(), name="create-post"),
    path('edit_post/<slug:slug>', views.EditPost.as_view(), name="edit-post"),
    path('post/<slug:slug>/delete', views.DeletePost.as_view(), name="delete-post"),
    path('like/<int:pk>', views.LikeView, name="like-post"),
    path('post/<slug:slug>/comment', views.CreateCommentView.as_view(), name="create-comment"),
]

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Profile, Comment
from rest_framework import viewsets
from django.http import HttpResponseRedirect
from django.urls import reverse
from .serializers import *
from rest_framework_swagger.views import get_swagger_view


# Create your views here.


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


"""
class CreatePost(generic.CreateView):
    model = Post
    template_name = "create_post.html"
    fields = ("title", "content")


class EditPost(generic.UpdateView):
    model = Post
    template_name = "edit-post.html"
    fields = ("title", "content")


class DeletePost(generic.DeleteView):
    model = Post
    template_name = "delete_post.html" """


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

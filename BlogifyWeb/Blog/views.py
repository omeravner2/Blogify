from django.shortcuts import render, get_object_or_404
from .models import Post, Profile, Comment
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views import generic
from .serializers import *


# Create your views here.


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def likes(self, request, pk=None):
        post = self.get_object()
        likes = post.likes.values()
        print(likes)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

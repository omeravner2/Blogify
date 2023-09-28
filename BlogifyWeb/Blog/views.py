from django.shortcuts import render, get_object_or_404
from .models import Post, Profile, Comment
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views import generic
from .serializers import *
from django.http import JsonResponse
from django.dispatch import receiver
from django.db.models.signals import post_save


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
        liking_users = post.likes.all()
        usernames = [user.username for user in liking_users]
        usernames = {'usernames': usernames}
        return JsonResponse(usernames)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=True, methods=['GET'])
    def posts(self, request, pk=None):
        profile = self.get_object()
        user = profile.user
        posts = Post.objects.filter(author=user)
        serializer = PostProfileSerializer(posts, many=True)
        return Response(serializer.data)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

from django.shortcuts import render, get_object_or_404
from .models import Post, Profile, Comment
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.views import generic
from .serializers import *
from django.http import JsonResponse
from django.dispatch import receiver
from django.db.models.signals import post_save
import json


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
        users = [user.id for user in liking_users]
        usernames = [user.username for user in liking_users]
        usernames = {'usernames': usernames, 'users_id': users}
        return JsonResponse(usernames)

    @action(detail=True, methods=['patch'])
    def toggle_like(self, request, pk=None,  user_id=None):
        post = self.get_object()
        user = User.objects.get(id=user_id)
        remove = False
        add = False
        if user in post.likes.all():
            post.likes.remove(user)
            remove = True
        else:
            post.likes.add(user)
            add = True
        liking_users = post.likes.all()
        users = [user.id for user in liking_users]
        usernames = [user.username for user in liking_users]
        usernames = {'usernames': usernames, 'users_id': users}
        if remove:
            return Response({'message': 'Post unliked', 'data': usernames}, status=200)
        elif add:
            return Response({'message': 'Post liked', 'data': usernames}, status=200)



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

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        profile = ProfileSerializer(profile, context={'request': request}).data
        posts = Post.objects.filter(author=user).order_by('-created_on')
        serializer = PostSerializer(posts, context={'request': request}, many=True)
        data = {'profile': profile, 'posts': serializer.data}
        return Response(data)


@api_view(['GET'])
def posts_list(request):
    userid = request.GET.get('userid')
    posts = Post.objects.all().order_by('-created_on')
    data = []
    list_of_posts = []
    for post in posts:
        post_author = post.author
        print("post-author " + str(post_author))
        matching_profile = Profile.objects.get(user=post_author)
        profile_pic = ProfilePicSerializer(matching_profile, context={'request': request}).data
        post_data = PostSerializer(post, context={'request': request}).data
        post_data.update(profile_pic)
        list_of_posts.append(post_data)
    data.append({'posts': list_of_posts, 'user_profile': current_user(userid, request)})
    return Response(data)


def current_user(userid, request):
    matching_profile = Profile.objects.get(user=userid)
    serializer = ProfileSerializer(matching_profile,  context={'request': request})
    return serializer.data


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

from rest_framework import serializers
from .models import Post, Comment, Profile
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CommentDetailsSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ('author_name', 'body', 'created_on')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')

    class Meta:
        model = Profile
        fields = ('id', 'bio', 'profile_picture', 'username', 'first_name', 'last_name')


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'username'



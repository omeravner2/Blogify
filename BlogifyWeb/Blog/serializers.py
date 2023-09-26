from rest_framework import serializers
from .models import Post, Comment, Profile
from BlogifyWeb.accounts.serializers import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'bio', 'profile_picture', 'user.name')

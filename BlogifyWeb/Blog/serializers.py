from rest_framework import serializers
from .models import Post, Comment, Profile
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.ReadOnlyField(source='get_likes_count')

    class Meta:
        model = Post
        fields = ['title', 'id', 'author', 'content', 'photo', 'created_on', 'likes_count']
        read_only_fields = ['slug']

    def to_representation(self, instance):
        request = self.context.get('request')
        data = super().to_representation(instance)
        if instance.photo:
            data['photo'] = request.build_absolute_uri(instance.photo.url)
        return data


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ('author_name', 'body', 'created_on', 'author', 'id', 'post')




class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')

    class Meta:
        model = Profile
        fields = ('id', 'bio', 'profile_picture', 'username', 'first_name', 'last_name')

    def to_representation(self, instance):
        request = self.context.get('request')
        data = super().to_representation(instance)
        if instance.profile_picture:
            data['profile_picture'] = request.build_absolute_uri(instance.profile_picture.url)
        return data


class ProfilePicSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = ['profile_picture', 'username']

    def to_representation(self, instance):
        request = self.context.get('request')
        data = super().to_representation(instance)
        if instance.profile_picture:
            data['profile_picture'] = request.build_absolute_uri(instance.profile_picture.url)
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class LikeSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True)

    class Meta:
        model = Post
        fields = ['likes']


class PostProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_on']


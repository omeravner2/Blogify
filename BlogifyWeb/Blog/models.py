from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', editable=True, always_update=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to="images/Posts/")
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blog_posts", blank=True)

    def get_likes_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, str(self.author))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/Profiles/")

    def __str__(self):
        return str(self.user) + " | " + str(self.bio)

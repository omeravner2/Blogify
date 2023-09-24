from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.

class HomePageView(generic.ListView):
    model = Post
    template_name = 'homepage.html'
    ordering = ['-created_on']


class PostView(generic.DetailView):
    model = Post
    template_name = "post_details.html"


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
    template_name = "delete_post.html"

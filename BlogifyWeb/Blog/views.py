from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

class HomePageView(generic.ListView):
    model = Post
    template_name = 'homepage.html'
    ordering = ['-created_on']

    def get_context_data(self, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs)
        total_likes = post.get_likes_count()
        liked = False
        if post.likes.filter(id=self.request.user.id).exist():
            liked = True
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context["total_likes"] = total_likes
        context["liked"] = liked


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


def LikeView(request, pk):
    post = Post.objects.get(id=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exist():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("post-details", args=[str(pk)]))


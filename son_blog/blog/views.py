from django.shortcuts import render

# Create your views here.
from blog.models import Post # noqa


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def post(request, post_id):
    posts = Post.objects.get(pk=post_id) # noqa
    return render(request, 'post.html', {'posts': post})

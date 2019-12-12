from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
import os

from django.urls import reverse

# Create your views here.

from blog.models import Post


def post_list(request):
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts,
    }

    return render(request, 'post_list.html', context)

def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'post_detail.html', context)


def post_add(request):

    if request.method == 'POST':
        author = request.user
        title = request.POST["title"]
        text = request.POST["text"]

        post = Post.objects.create(
            author = author,
            title = title,
            text = text,
        )

        result = f'title: {post.title}, created_date: {post.created_date}'

        return redirect('url-name-post-list')

    else:

        return render(request, 'post_add.html')
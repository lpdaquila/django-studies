# from django.http import HttpResponse
from typing import Any
from django.http import Http404, HttpRequest
from django.shortcuts import render
from . import data

# Create your views here.
def blog(request):
    context = {
        'text': 'We are in blog',
        'posts': data.posts
    }
    
    return render(
        request,
        'blog/index.html',
        context
    )
    
def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None
    for post in data.posts:
        if post['id'] == post_id:
            found_post = post
            break
            
    if found_post is None:
        raise Http404('Post not found')
    
    context = {
        # 'text': 'We are in blog',
        'post': found_post,
        'title': found_post['title'] + ' | '
    }
    
    return render(
        request,
        'blog/post.html',
        context
    )

def example(request):
    
    context = {
        'text': 'We are in example',
    }
    
    return render(
        request,
        'blog/example.html',
        context
    )
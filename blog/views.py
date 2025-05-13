# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog(request):
    context = {
        'text': 'We are in blog'
    }
    
    return render(
        request,
        'blog/index.html',
        context
    )

def example(request):
    
    context = {
        'text': 'We are in example'
    }
    
    return render(
        request,
        'blog/example.html',
        context
    )
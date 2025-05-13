from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog(request):
    return HttpResponse('blog1')

def example(request):
    return HttpResponse('blog example')
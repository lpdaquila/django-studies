# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    
    context = {
        'text': 'We are in home',
        'title': 'Homepage | '
    }
    
    return render(
        request,
        'home/index.html',
        context
    )
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/<int:post_id>/', views.post, name='post'),
    path('posts/', views.blog, name='home'),
    path('example/', views.example, name='example')
]
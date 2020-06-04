from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Post

# Create your views here.


class PostCreateView(CreateView):
    model = Post
    # fields = ('message', 'group')
    fields = '__all__'


class PostListView(ListView):
    model = Post

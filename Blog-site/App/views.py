from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post
# Create your views here.
""" def home(request):
    return render(request, 'App/index.html') """
""" 
def posts(request):
    return render(request, 'App/posts.html') """
# using class views

class PostView(ListView):
    model = Post
    template_name = "App/posts.html"

class HomeViews(ListView):
    model = Post
    template_name = 'App/index.html'
    
class SinglePostView(DetailView):
    model = Post
    template_name = 'App/singlepost.html'
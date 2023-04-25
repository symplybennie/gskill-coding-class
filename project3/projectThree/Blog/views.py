from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . models import Post

# Create your views here.
class PostView(ListView):
    model = Post
    template_name = 'blog/blog.html'

""" def addPostView(request):
    posts = Post.objects.all()
    template = 'blog/addpost.html'
    return render(request, template, {'posts': posts}) """

class addPostView(CreateView):
    model = Post
    template_name = 'blog/addpost.html'
    fields = '__all__'

""" class singlePostView(DetailView):
    model = Post
    template_name = 'blog/singlepost.html' """
    
def singlePostView(request, pk):
    post = Post.objects.get(id=pk)
    context ={
        'post': post
    }
    return render(request, 'blog/singlepost.html', context)
from django.shortcuts import render
# from django.views.generic import ListView, DetailView
# from django.http import HttpResponse
# from django.template import loader
from . models import Post

# Create your views here.
""" def home(request):
    return render(request, 'blog/index.html')
def blog(request):
    return render(request, 'blog/posts.html')
def contact(request):
    return render(request, 'blog/contact.html') """

""" class HomeViews(ListView):
    model = Post
    template_name = 'blog/index.html'
    
class PostViews(ListView):
    model = Post
    template_name = 'blog/posts.html'

class ContactViews(ListView):
    model = Post
    template_name = 'blog/contact.html'
    
class SinglePostViews(DetailView):
    model = Post
    template_name = 'blog/singlepost.html' """

def home(request):
    mypost = Post.objects.all()
    return render(request, 'blog/index.html', {'post': mypost})
    # return HttpResponse(template.render(context, request))

def blog(request, pk):
    mypost = Post.objects.get(id=pk)
    return render(request, 'blog/posts.html', {'post': mypost})
    # return HttpResponse(template.render(context, request))


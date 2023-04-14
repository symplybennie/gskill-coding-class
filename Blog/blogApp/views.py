from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
""" def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
"""

posts =[
    {
        'author': 'Benny',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'James',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogApp/home.html', context)

def about(request):
    return render(request, 'blogApp/about.html', {'title': 'About'})

""" def services(request):
    return HttpResponse('<h1>Services Page</h1>') """

from django.contrib import admin
from django.urls import path, include



""" def hello(request, work):
    return HttpResponse('<h1>Hello Django! ' + work + '</h1>')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

 """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appintro.appurls')),
    path('', include('apptest.testurls')),
  
]

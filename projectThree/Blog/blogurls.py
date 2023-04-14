from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('categories/', views.categories, name='categories'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:work>/', views.hello, name='hello'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('student/<int:work>/', views.student, name='student')
]
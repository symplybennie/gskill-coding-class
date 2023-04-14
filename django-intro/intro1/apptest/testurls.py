from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.services, name='services'),
    path('product/', views.product, name='product'),
    path('about/', views.about, name='about')
]
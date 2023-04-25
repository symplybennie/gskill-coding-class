from django.urls import path
from . import views

urlpatterns = [
    path('', views.benny, name='benny'),
    path('index/', views.index, name='index'),
    path('page/', views.page, name='page'),
]
# path('<str:name>', views.greet, name='greet'),
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='blog'),
    path('addpost/', views.addPostView.as_view(), name='addPost'),
    path('singlepost/<int:pk>', views.singlePostView, name='singlePost')
]
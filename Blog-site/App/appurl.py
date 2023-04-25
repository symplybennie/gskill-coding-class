from django.urls import path
from . import views
# from .views  import HomeViews

urlpatterns = [
    path('', views.HomeViews.as_view(), name='home'),
    path('posts/', views.PostView.as_view(), name='posts'),
    path('singlepost/<int:pk>', views.SinglePostView.as_view(), name='singlepost')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('singleproduct/', views.singleproduct, name='singleproduct'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
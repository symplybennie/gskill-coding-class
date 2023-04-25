from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('details/<int:pk>', views.Details.as_view(), name='details'),
    path('addmembership/', views.AddMembership.as_view(), name='addmembership'),
    path('agepage/', views.AgePageView.as_view(), name='agepage')
]
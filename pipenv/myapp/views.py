from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . models import Member
from django.urls import reverse_lazy
# Create your views here.

class HomeView(ListView):
    model = Member
    template_name = 'myapp/index.html'

class Details(DetailView):
    model = Member
    template_name = 'myapp/details.html'

class AddMembership(CreateView):
    model = Member
    template_name = 'myapp/addmembership.html'
    fields = '__all__'
    # fields = ['firstname', 'lastname', 'age']
    # success_url = reverse_lazy('home')
    
class AgePageView(ListView):
    model = Member
    template_name = 'myapp/agepage.html'
from django.shortcuts import render

# Create your views here.
def services(request):
    return render(request, 'apptest/services.html')

def product(request):
    return render(request, 'apptest/product.html')

def about(request):
    return render(request, 'apptest/about.html')
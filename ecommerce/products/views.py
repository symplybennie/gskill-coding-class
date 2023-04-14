from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'products/index.html')

def shop(request):
    return render(request, 'products/shop.html')
    
def cart(request):
    return render(request, 'products/cart.html')

def checkout(request):
    return render(request, 'products/checkout.html')

def singleproduct(request):
    return render(request, 'products/singleproduct.html')

def signup(request):
    return render(request, 'products/signup.html')

def login(request):
    return render(request, 'products/login.html')

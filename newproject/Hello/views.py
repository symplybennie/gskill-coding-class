from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
import calendar
# Create your views here.

def benny(request):
    return HttpResponse('Hello Benny')

"""
def david(request):
    return HttpResponse('Hello David')

def andrew(request):
    return HttpResponse('Hello Andrew') 

def greet(request, name):
    return HttpResponse(f'Hello {name}')
"""
def index(request):
    ages = [14, 19, 20, 40, 18, 17, 30, 35, 29, 28, 32]
    context = {
        'ages': ages
    }
    return render(request, 'hello/index.html', context)

def page(request):
    return render(request, 'hello/page.html')

def weekday(request):
    day = date.today()
    monday = day.weekday() == 0
    tuesday = day.weekday == 1
    wednesday = day.weekday() == 2
    thursday = day.weekday() == 3
    friday = day.weekday() == 4
    saturday = day.weekday() == 5
    sunday = day.weekday() == 6
    times = datetime.now.strftime("%H%p, 5B %d, %Y")
    context = {
        'monday': monday,
        'tuesday': tuesday,
        'wednesday': wednesday,
        'thursday': thursday,
        'friday': friday,
        'saturday': saturday,
        'sunday': sunday,
        'time': times
    }
    return render(request, 'hello/weekday.html', context)

def newyear(request):
    day = date.today()
    january = day.month() == 0
    february = day.month() == 1
    march = day.month() == 2
    april = day.month() == 3
    may = day 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
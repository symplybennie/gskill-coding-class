from django.shortcuts import render
from django.http import HttpResponse

stud_db = [
    {
        'id': 1,
        'name': 'Benny',
        'course': 'python',
        'score': 90
    },
     {
        'id': 2,
        'name': 'Dave',
        'course': 'nodejs',
        'score': 80
    },
     {
        'id': 3,
        'name': 'Samuel',
        'course': 'Javascript',
        'score': 70
    },
     {
        'id': 4,
        'name': 'Andrew',
        'course': 'PHP',
        'score': 70
    },
]

# Create your views here.
def hello(request, work):
    return HttpResponse('<h1>Hello Django! ' + work + '</h1>') 

def student(request, work):
    stu_info = None
    for i in stud_db:
        if i ['id'] == work:
            stu_info = i
    return render(request, 'appintro/student.html', {'studs': stu_info})

def home(request):
    page = 'Landing Page'
    age = 19
    context = {
        'msg': page, 
        'years_old': age,
        'student_data': stud_db
        }
    return render(request, 'appintro/index.html', context)

def about(request):
    page = 'About Us Page'
    return render(request, 'appintro/about.html', {'msg': page})


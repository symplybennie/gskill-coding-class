from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    DOB = models.DateTimeField()
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def get_absolute_url(self):
        return reverse('home')

    

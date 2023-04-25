from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return f'{self.author} - {self.title}'
    
    def get_absolute_url(self):
        return reverse('blog')

import uuid
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title
        
from django.db import models
from datetime import datetime
 
# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=80)
    content = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now)
 
    def __str__(self):
        return self.name

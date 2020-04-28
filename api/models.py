from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class UserProgress(models.Model):
    title = models.TextField(max_length=32,blank=False,null=False)
    magicscore = models.IntegerField(blank=True,null=True) 
    present = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Dormitory(models.Model):
    title = models.TextField(max_length=32,blank=False,null=False)
    mags = models.ManyToManyField(UserProgress, related_name="mags")
    
    def __str__(self):
        return self.title
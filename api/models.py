from django.db import models
from django.contrib.auth.models import User


class UserProgress(models.Model):
    title = models.TextField(max_length=32,blank=False,null=False)
    magicscore = models.IntegerField(blank=True,null=True) 
    present = models.BooleanField(default=False,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Dormitory(models.Model):
    title = models.TextField(max_length=32,blank=False,null=False)
    mags = models.ManyToManyField(UserProgress, related_name="mags")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
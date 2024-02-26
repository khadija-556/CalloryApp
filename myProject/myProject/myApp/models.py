from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER =(
        ('male','Male'),
        ('female','Female'),
    )
    name = models.CharField(max_length = 100, null=True)
    gender = models.CharField(choices=GENDER, max_length = 100, null=True)
    age = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    BMR = models.FloatField(null = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
class callory(models.Model):
    iteam=models.CharField(max_length = 100, null=True)
    callory=models.FloatField(null=True)
    date = models.DateField(null = True , auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True , blank = True)

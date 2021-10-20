from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(blank = False, default=None, null=True)
    date_enrolled = models.DateTimeField(auto_now =True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, default=None, null= True)
    def __str__(self):
        return self.name
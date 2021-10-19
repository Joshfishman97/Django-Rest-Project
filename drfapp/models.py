from django.db import models

# Create your models here.
class Student(model.models):
    name = models.CharField(max_length=100)
    age = models.IntergetField()
    description = models.IntergetField()
    date_enrolled = models.DateTimeField()
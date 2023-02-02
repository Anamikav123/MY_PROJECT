from django.db import models

# Create your models here.
class TeacherModel(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.IntegerField()
    qualification=models.CharField(max_length=40)

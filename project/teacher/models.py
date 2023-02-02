from django.db import models

# Create your models here.
class StudentModel(models.Model):
    first=models.CharField(max_length=50)
    last=models.CharField(max_length=50)
    age=models.IntegerField()
    Address=models.CharField(max_length=500)
    phone=models.IntegerField()
    email=models.EmailField()
    roll_no=models.IntegerField(null=True)


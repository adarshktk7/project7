from django.db import models
from django.contrib.auth.models import AbstractUser


class user(AbstractUser):
    usertype=models.CharField(max_length=100)

class department(models.Model):
    dep_name=models.CharField(max_length=100)


class Teacher(models.Model):
    depid=models.ForeignKey(department,on_delete=models.CASCADE)
    tid=models.ForeignKey(user,on_delete=models.CASCADE)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)

class Student(models.Model):
    depid=models.ForeignKey(department,on_delete=models.CASCADE)
    sid=models.ForeignKey(user,on_delete=models.CASCADE)
    age=models.IntegerField()
    address=models.CharField(max_length=100)

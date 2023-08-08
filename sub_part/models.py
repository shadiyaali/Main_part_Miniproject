from django.db import models
from django.forms import CharField

# Create your models here.

class userdata(models.Model):
        
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    
    def __str__(self):
       return self.username

class image_data(models.Model):
    pname = models.CharField(max_length=50)
    pimage = models.FileField(default=0)

    def __str__(self):
        return self.pname

class Student(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class Book(models.Model):
    
    name = models.CharField(max_length=100)
    page = models.IntegerField()
    auther = models.CharField(max_length=100)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
     

    def __str__(self):
        return self.name


        


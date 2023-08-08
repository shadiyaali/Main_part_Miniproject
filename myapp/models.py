from django.db import models

# Create your models here.



class Employee(models.Model):
    id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)



class Department(models.Model):
    department_id = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee,on_delete=)

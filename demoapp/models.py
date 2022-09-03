from django.db import models

# Create your models here.
class EmployeesData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    salary=models.IntegerField()
    company=models.CharField(max_length=50)
    locaton=models.CharField(max_length=50)
    

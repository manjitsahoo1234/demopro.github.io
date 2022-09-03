from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import EmployeesData

# Create your views here.
def homepage(request):
    return render(request,'index.html')

from django.shortcuts import render
from .models import *

# Create your views here.

def get_students(request):
    queryset = Student.objects.all()
    
    return render(request, 'students.html', {'queryset': queryset})
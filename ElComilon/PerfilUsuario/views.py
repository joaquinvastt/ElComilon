from django.shortcuts import render
from Login.models import Cliente

# Create your views here.
def Usertemplate(request): 
    nombre = "Juan"
    return render(request, 'User.html')

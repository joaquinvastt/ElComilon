from django.shortcuts import render

# Create your views here.
def register (reques):
    return render(reques,'registerUser.html')

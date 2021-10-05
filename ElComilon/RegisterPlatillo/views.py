from django.shortcuts import render

# Create your views here.
def registroPlatillo (request):
    return render(request,'registrarPlatillo.html')
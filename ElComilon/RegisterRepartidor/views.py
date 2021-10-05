from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
import cx_Oracle
from core.models import *


# Create your views here.
def RegisterRepatidor(request): 

    # agregar_repartidor('203211058','Juan carlo', 'PEREZ PEREZ', '20-03-2021','Jcarlos', 'Jcarlos123','203453423')
    return render(request, 'Registrorepartidor.html')

def registroRep(request):
    print("ENtrada")

    if request.method == 'POST':
        RUTREPARTIDOR = request.POST.get('RutRepartidor')
        NOMBRES = request.POST.get('NombresRepartido')
        Apellido = request.POST.get('ApellidosRepartidor')
        Fechacontrato = request.POST.get('Fechacontrato')
        Usuario = request.POST.get('Usuario')
        Contrasena = request.POST.get('contrasena')
        Rutempresa = request.POST.get('rutempresa')
        Patente = request.POST.get('Patente')
        Modelo = request.POST.get('Modelo')
        Ano = request.POST.get('Ano')
        Color = request.POST.get('Color') 


        
        
    


def agregar_repartidor(RUTREPARTIDOR, NOMBRES, APELLIDOS, FECHACONTRATO, USUARIO, CONTRASENA, RUTRESTAURANTE):
     django_cursor = connection.cursor()
     cursor = django_cursor.connection.cursor()   
     salida = cursor.var(cx_Oracle)    
     cursor.callproc('SP_AGREGAR_REPARTIDOR', [RUTREPARTIDOR,NOMBRES,APELLIDOS,FECHACONTRATO,USUARIO,CONTRASENA,RUTRESTAURANTE, salida])
     return salida.getvalue()   

def agregar_vehiculo(PATENTEVEHICULO, MODELO, ANIO, COLOR, RUTREPARTIDOR, IDTIPOVEHICULO):
     django_cursor = connection.cursor()
     cursor = django_cursor.connection.cursor()   
     salida = cursor.var(cx_Oracle)    
     cursor.callproc('SP_AGREGAR_VEHICULO', [PATENTEVEHICULO,MODELO,ANIO,COLOR,USUARIO,RUTREPARTIDOR,IDTIPOVEHICULO, salida])
     return salida.getvalue()        
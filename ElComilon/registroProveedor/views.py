from django.shortcuts import render
from django.db import connection
import cx_Oracle

# Create your views here.

def registroProveedor (request):
    data = {
        'tipo':listar_tipoRestaurante(),
        'representante':listar_representante()
    }
    if request.method == 'POST':
        rutRest = request.POST.get('rutRestaurante').upper()
        nombre = request.POST.get('nombre').upper()
        direccion = request.POST.get('direccion').upper()
        representante =  request.POST.get('representante').upper()
        tipo = 1
        salida = registrar (rutRest,nombre,direccion,representante,tipo)
        if salida == 1 :
            data['mensaje'] = 'Agregado correctamente'
        else:
            data['mensaje'] = 'No se ha podido guardar'

    #registrar('77.684.134-5','McDonald','chile','19.471.008-0',1)
    return render (request,'registro-proveedor.html',data)

def listar_tipoRestaurante():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("LISTAR_TIPO_RESTAURANTE",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def listar_representante():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("LISTAR_REPRESENTANTE",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def registrar(rutRest, nombreRest, direccionRest, rutRepresentante, idTipo):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("REGISTRAR_PROVEEDOR",[rutRest, nombreRest, direccionRest, rutRepresentante, idTipo, salida])
    return salida.getvalue()



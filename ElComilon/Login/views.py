from django.shortcuts import render

# Create your views here.
def login (request):
    return render(request,'iniciar_sesion.html')
 
def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = formLog(request.POST)
        if formulario is valid:
            nombreusuario = request.POST['nombreusuario']
            contrasena = request.POST['contrasena']
            
            verificacion = Cliente.objects.filter(nombreusuario=nombreusuario, contrasena=contrasena).exists()
            print(verificacion)
            
            if verificacion is True:
                return print("valido")
            else:
                return print("valido")
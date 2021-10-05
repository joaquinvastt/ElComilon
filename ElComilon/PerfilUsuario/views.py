from django.shortcuts import render
from Login.models import Cliente

# Create your views here.
def Usertemplate(request): 
    nombre = "Juan"
    ctx = Context ({"nombre_persona":nombre})
    documento = plt.render(ctx)
    return render(request, 'User.html')

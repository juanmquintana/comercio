from django.shortcuts import render

from .models import Productos

def listar(request):
    template_name = "productos/listar.html"
    ctx = {
        "nombre_usuario": "Juan Manuel",
        "lista_productos": Productos.objects.all().order_by("-id")#trae todos
        #"lista_productos": Productos.objects.filter(id=2) #trae solo uno
        #"lista_productos": Productos.objects.filter(nombre="Cargador USB") #trae solo uno
        #"lista_productos": Productos.objects.filter(nombre="Cargador USB").order by("nombre","id")#first() #trae solo uno
        #"lista_productos": Productos.objects.get(id=2)
    }
    return render(request,template_name,ctx)
    '''
    Si usamos get() devuelve un elemento, en el caso de dos productos
    con el mismo nombre devolveria y daria error.
    Cuando necesitamos que devuelvan varios usamos el filter()
    '''

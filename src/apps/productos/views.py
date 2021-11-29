from django.shortcuts import render

from .models import Productos

def listar(request):
    template_name = "productos/listar.html"
    ctx = {
        "nombre_usuario": "Juan Manuel",
        "lista_productos": Productos.objects.all()
    }
    return render(request,template_name,ctx)

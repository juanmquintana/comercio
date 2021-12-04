from django.shortcuts import render

from apps.productos.models import Productos

def inicio(request):
    template_name = "index.html"
    ''' para ver que me devuelve el contex en la consola hago un print
    -id significa orden descendente
    [:2] es un corte sobre la lista y le digo que me retorne los ultimos dos elementos
    '''
    ultimos_productos = Productos.objects.all().order_by('-id') [:2]
    #print(ultimos_productos)
    ctx = {
        'ultimos_productos': ultimos_productos
    }
    return render(request,template_name,ctx)
'''**** reemplazamos la vista basada en funcion por vista basada en clase 
def login(request):
    template_name = "login.html"
    ctx = {}
    return render(request,template_name,ctx)
'''

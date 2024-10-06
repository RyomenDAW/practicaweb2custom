from django.shortcuts import render
from .models import Personaje, Hechicero, Marginado, Piromano, Dexteridad

# Create your views here.
def personaje_list(request):
    personaje = Personaje.objects.all()
    return render(request, 'personajes/personaje_list.html',{'personaje_mostrar': personaje})

def hechicero_list(request):
    hechicero = Hechicero.objects.all()
    return render(request, 'hechiceros/hechicero_list.html',{'hechicero_mostrar': hechicero})

def marginado_list(request):
    marginado = Marginado.objects.all()
    return render(request, 'marginados/marginado_list.html',{'marginado_mostrar': marginado})

def piromano_list(request):
    piromano = Piromano.objects.all()
    return render(request, 'piromanos/piromano_list.html',{'piromano_mostrar': piromano})

def dexteridad_list(request):
    dexteridad = Dexteridad.objects.all()
    return render(request, 'dexteridad/dexteridad_list.html',{'dexteridad_mostrar': dexteridad})

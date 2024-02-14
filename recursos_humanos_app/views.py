from django.shortcuts import render

# Create your views here.

def crearTrabajador(request):
    return render(request, "crearTrabajador.html")

def eliminarTrabajador(request):
    return render(request, "eliminarTrabajador.html")   
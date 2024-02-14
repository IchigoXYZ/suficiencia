from django.shortcuts import render

# Create your views here.

def crearTrabajador(request):
    return render(request, "crearTrabajador.html")

def eliminarTrabajador(request):
    return render(request, "eliminarTrabajador.html")   

def listar_trabajadores(request):
    tipo_trabajador = request.GET.get('tipo_trabajador', None)
    trabajadores = []

    if tipo_trabajador == 'docente':
        trabajadores = TrabajadorDocente.objects.all()
    elif tipo_trabajador == 'no_docente':
        trabajadores = TrabajadorNoDocente.objects.all()

    return render(request, 'listarTrabajadores.html', {'trabajadores': trabajadores})

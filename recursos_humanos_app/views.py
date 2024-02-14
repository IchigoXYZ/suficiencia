from django.shortcuts import render

# Create your views here.

def crearTrabajador(request):
    return render(request, "crearTrabajador.html")

def eliminar_trabajador(request):
    if request.method == 'POST':
        carnet_identidad = request.POST.get('carnet_identidad')
        try:
            trabajador = Trabajador.objects.get(carnet_identidad=carnet_identidad)
            trabajador.delete()
            mensaje = f"El trabajador con carné de identidad {carnet_identidad} ha sido eliminado correctamente."
        except Trabajador.DoesNotExist:
            mensaje = f"No se encontró ningún trabajador con el carné de identidad {carnet_identidad}."
        return render(request, 'eliminar_trabajador.html', {'mensaje': mensaje})
    return render(request, 'eliminar_trabajador.html') 

def listar_trabajadores(request):
    tipo_trabajador = request.GET.get('tipo_trabajador', None)
    trabajadores = []

    if tipo_trabajador == 'docente':
        trabajadores = TrabajadorDocente.objects.all()
    elif tipo_trabajador == 'no_docente':
        trabajadores = TrabajadorNoDocente.objects.all()

    return render(request, 'listarTrabajadores.html', {'trabajadores': trabajadores})

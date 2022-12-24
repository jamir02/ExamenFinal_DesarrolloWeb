from django.shortcuts import render
from django.urls import reverse
from .models import tareasExamen, usuariosFinal
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        #Validacion de informacion
        usuario_registrado = 0
        usuarios_totales = usuariosFinal.objects.all()

        for usuario in usuarios_totales:
            if usuario.usuario == nombreUsuario and usuario.contra == passwordUsuario:
                usuario_registrado = 1
        
        if usuario_registrado == 1:
            return HttpResponseRedirect(reverse('examenFinal:dashboard'))
        else:
            return render(request,'examenFinal/ingresar.html',{
                'mensaje':'Los datos ingresados son incorrectos',
            })
    return render(request,'examenFinal/ingresar.html')

def dashboard(request):
    return render(request,'examenFinal/dashboard.html',{
        'tareas_totales':tareasExamen.objects.all().order_by('id')
    })
#Obtengo la información de la tarea
def obtener_info_tarea(request):
    datoTarea = str(request.GET.get('tarea')) #obtengo el identificador
    infoTarea = tareasExamen.objects.get(id=datoTarea) #obtengo la info de la tarea seleccionada
    arregloTarea = [infoTarea.fechaCreacion, infoTarea.fechaEntrega, infoTarea.descripcion, infoTarea.estadoTarea] #coloco la información en un arreglo
    print(datoTarea)
    return JsonResponse({
        'dato': arregloTarea, # paso los datos de la tarea seleccionada a la parte front
    })
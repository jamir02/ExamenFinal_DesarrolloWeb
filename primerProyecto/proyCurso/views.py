from django.shortcuts import render
from .models import producto,solicitud
from django.http import HttpResponseRedirect,JsonResponse, HttpResponse
from django.urls import reverse
import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Create your views here.
def descargar_solicitud(request,ind):
    solicitu_info = solicitud.objects.get(id=ind)
    pdf_name = 'solicitud.pdf'
    can = canvas.Canvas(pdf_name,pagesize=A4)
    can.setFillColorRGB(0,0,0)
    can.setFont('Helvetica',12)
    can.drawString(20,785,solicitu_info.codigoSolicitud)
    infoProductos = solicitu_info.nombreProductos.split(',')
    infoCantidad = solicitu_info.cantidadProductos.split(',')
    i= 0
    coor_y = 750
    for producto in infoProductos:
        can.drawString(20,coor_y,producto)
        can.drawString(120,coor_y,infoCantidad[i])
        coor_y = coor_y - 20
        i = i + 1
    can.showPage()
    can.save()
    nombre_doc = solicitu_info.codigoSolicitud + '.pdf'
    reponse = HttpResponse(open('solicitud.pdf','rb'),content_type='application/pdf')
    nombre = 'attachment; + filename=' + nombre_doc
    reponse['Content-Disposition'] = nombre
    return reponse

def dashboard(request):
    productos_totales = producto.objects.all()
    return render(request,'proyCurso/dashboard.html',{
        'productos_totales':productos_totales
    })

def vistaProd(request,ind):
    producto_seleccionado = producto.objects.get(id=ind)
    return render(request,'proyCurso/vistaProd.html',{
        'producto_seleccionado':producto_seleccionado
    })

def eliminarProd(request,ind):
    producto_eliminar = producto.objects.get(id=ind)
    producto_eliminar.delete()
    return HttpResponseRedirect(reverse('proyCurso:dashboard'))

def obtenerInfo(request):
    datoProducto = str(request.GET.get('producto'))
    infoProducto = producto.objects.get(id=datoProducto)
    arregloProducto = [infoProducto.id,infoProducto.nombre,infoProducto.precio,infoProducto.descripcion,infoProducto.estado,infoProducto.stock]
    return JsonResponse({
        'dato':arregloProducto,
    })

def verSolicitudes(request):
    solicitudesTotales = solicitud.objects.all().order_by('-id')
    return render(request,'proyCurso/verSolicitudes.html',{
        'solicitudes':solicitudesTotales,
    })

def crearSolicitud(request):
    productos_totales = producto.objects.all().order_by('id')
    return render(request,'proyCurso/crearSolicitud.html',{
        'productos':productos_totales
    })

def agregarSolicitud(request):
    if request.method == 'POST':
        datos = json.load(request)
        arregloProductos = datos.get('productosCapturados')
        cliente = datos.get('cliente')
        print(arregloProductos)
        nombresProductos = ''
        cantidadesProductos = ''
        idenProductos = ''
        for producto in arregloProductos:
            idenProductos = idenProductos + ',' + producto[0]
            nombresProductos = nombresProductos + ',' + producto[1]
            cantidadesProductos = cantidadesProductos + ',' + producto[2]
        nombresProductos = nombresProductos[1:]
        cantidadesProductos = cantidadesProductos[1:]
        idenProductos = idenProductos[1:]
        solicitud(idProductos=idenProductos,nombreProductos=nombresProductos,cantidadProductos=cantidadesProductos,cliente=cliente).save()
        print(nombresProductos)
        print(cantidadesProductos)
        print(idenProductos)
        solicitud_mod = solicitud.objects.latest('id')
        id_solicitud = str(solicitud_mod.id)
        while len(id_solicitud) < 4:
            id_solicitud = '0' + id_solicitud
        solicitud_mod.codigoSolicitud = 'SOL-' + id_solicitud
        solicitud_mod.save()
        return JsonResponse({
            'resp':'ok'
        })
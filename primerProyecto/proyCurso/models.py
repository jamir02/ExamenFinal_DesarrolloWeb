from django.db import models
import datetime

# Create your models here.
class producto(models.Model):
    nombre = models.CharField(max_length=64,default='')
    precio = models.CharField(max_length=32,default='')
    nombreImagen = models.CharField(max_length=64,default='')
    descripcion = models.CharField(max_length=512,default='')
    estado = models.CharField(max_length=64,default='')
    stock = models.CharField(max_length=32,default='')

class solicitud(models.Model):
    idProductos = models.CharField(max_length=256,default='')
    nombreProductos = models.CharField(max_length=512,default='')
    cantidadProductos = models.CharField(max_length=512,default='')
    fecha = models.DateField(default=datetime.datetime.now())
    cliente = models.CharField(max_length=128,default='Cliente')
    codigoSolicitud = models.CharField(max_length=128,default='SOL-0000')
from . import views
from django.urls import path

app_name='proyCurso'

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('vistaProd/<str:ind>',views.vistaProd,name='vistaProd'),
    path('eliminarProd/<str:ind>',views.eliminarProd,name='eliminarProd'),
    path('obtenerInfo',views.obtenerInfo,name='obtenerInfo'),
    path('verSolicitudes',views.verSolicitudes,name='verSolicitudes'),
    path('crearSolicitud',views.crearSolicitud,name='crearSolicitud'),
    path('agregarSolicitud',views.agregarSolicitud,name='agregarSolicitud'),
    path('descargar_solicitud/<str:ind>',views.descargar_solicitud,name='descargar_solicitud'),
]
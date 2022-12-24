from . import views
from django.urls import path

app_name = 'examenFinal'

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('obtener_info_tarea', views.obtener_info_tarea, name='obtener_info_tarea'),
    path('crear_tarea', views.crear_tarea, name='crear_tarea'),
    path('eliminar_tarea', views.eliminar_tarea,name = 'eliminar_tarea'),
    path('editar_tarea', views.editar_tarea, name='editar_tarea'),
]
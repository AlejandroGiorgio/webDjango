from django.urls import path
from AppCoder.views import *
#
urlpatterns = [
    path('', index),
    path('cursos/', curso),
    path('entregables/', entregables),
    path('estudiantes/', estudiantes), 
    path ('profesores/', profesores),
    path ('api_estudiantes/', api_estudiantes),
    path('buscarEstudiante/', buscarEstudiante ),
    path('create_estudiantes/', create_estudiantes),
    path('read_estudiantes/', read_estudiantes),
    path('uptate_estudiantes/', update_estudiantes),
    path('delete_estudiantes/<estudiante_email>', delete_estudiantes),
    path('editar_perfil/', editarPerfil)
]


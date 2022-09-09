from http.client import INSUFFICIENT_STORAGE
from django.urls import path
from AppCoder.views import *
#
urlpatterns = [
    path('', index),
    path('cursos/', curso),
    path('entregables/', entregables),
    path('estudiantes/', estudiantes), 
    path ('profesores/', profesores)
]


import email
import re
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import form_estudiantes
from AppCoder.models import Estudiante
from AppCoder.forms import form_estudiantes, UserCreationForm, UserRegisterForm, UserEdithForm
# Create your views here.

def index(request):
    return render(request, "index.html")

def curso(request):
    return render(request, "cursos.html")

def profesores(request):
    return render(request, "profesores.html")

def estudiantes(request):
    if request.method == "POST":
        estudiante=Estudiante(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email=request.POST['email'], password=request.POST['password'])
        estudiante.save()
        return render (request, "estudiantes.html")
    return render(request, "estudiantes.html")
def entregables(request):
    return render(request, "entregables.html")

def api_estudiantes(request):
    if request.method == "POST":
        formulario=form_estudiantes(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiante = Estudiante (nombre= informacion['nombre'], apellido= informacion['apellido'], email=informacion['email'])
            estudiante.save()
            return render(request, "api_estudiantes.html")
    else:
        formulario = form_estudiantes()
    return render(request, "api_estudiantes.html", {"formulario": formulario})
    
def buscarEstudiante(request):
    if request.GET["email"]:
        email=request.GET["email"]
        estudiantes = Estudiante.objects.filter(email__icontains = email)
        return render(request, "estudiantes.html", {"estudiantes": estudiantes})
    else:
        respuesta="No enviaste datos"
    return HttpResponse(respuesta)

def create_estudiantes(request):
    if request.method == 'POST':
        estudiante = Estudiante(nombre= request.POST["nombre"], apellido= request.POST["apellido"], email= request.POST["email"])
        estudiante.save()
    return render(request, "estudiantesCRUD/create_estudiantes.html")

def read_estudiantes(request):
    estudiantes = Estudiante.objects.all() #trae todo
    return render (request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes":estudiantes})

def update_estudiantes(request, estudiante_email):
    estudiante = Estudiante.objects.get(email=estudiante_email)

    if request.method == 'POST':
        formulario=form_estudiantes(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            estudiante.nombre=informacion['nombre']
            estudiante.apellido=informacion['apellido']
            estudiante.email=informacion['email']
            estudiante.save()
            estudiante=Estudiante.objects.all()
            read_estudiantes()
        else:
            formulario=form_estudiantes(initial={'nombre':estudiante.nombre, 'apellido':estudiante.apellido, 'email':estudiante.email})




def delete_estudiantes(request, estudiante_email):
    estudiante = Estudiante.objects.get(email = estudiante_email)
    estudiante.delete()

    estudiantes = Estudiante.objects.all()    
    return render(request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})

#def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)

            if user is not None:
                login(request, user)
                return render(request, "home.html")
            else:
                return render(request, "login.html", {'form':form})
        else:
            return render(request, "login.html", {'form':form})
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registro(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "index.html")
    form = UserCreationForm()
    return render(request, "registro.html", {'form': form})


#@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == 'POST':
        form = UserEdithForm(request.POST, instance = usuario)
        if form.is_valid():
        #datos que se van a actualizar
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
        else:
            return render (request, 'home.html', {'form':form})
    else:
        form = UserEdithForm(initial={'email':usuario.email, 'username': usuario.usename, 'fisrt_name':usuario.first_name, 'last_name': usuario.last_name})
        return render(request, 'editarPerfil.html', {'form':form, 'usuario':usuario})

def changepass(request):
    usuario = request.user
    if request.method == "POST":
        pass
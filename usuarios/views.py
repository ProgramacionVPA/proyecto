from django.shortcuts import render, redirect
from .forms import FormularioRegistro, FormularioRuta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Ruta


def inicio(request):
    return render(request, 'inicio.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormularioRegistro()
    return render(request, 'registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('inicio')
    return render(request, 'login.html')

def logout_usuario(request):
    logout(request)
    return redirect('inicio')

def listar_rutas(request):
    rutas = Ruta.objects.all().order_by('-fecha_creacion')
    return render(request, 'listar_rutas.html', {'rutas': rutas})


@login_required
def crear_ruta(request):
    if request.method == 'POST':
        form = FormularioRuta(request.POST)
        if form.is_valid():
            ruta = form.save(commit=False)
            ruta.usuario = request.user
            ruta.save()
            return redirect('listar_rutas')
    else:
        form = FormularioRuta()
    return render(request, 'crear_ruta.html', {'form': form})


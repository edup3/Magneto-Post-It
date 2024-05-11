from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpRequest
from . forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Vacante
from funciones import *

# Create your views here.
def espera(request:HttpRequest):
    if request.method == 'POST':
        nom_vacante = request.POST.get('nombre-vacante')
        desc = request.POST.get('descripcion')
        disp = request.POST.get('vacantes-disp')
        salario = request.POST.get('salario')
        ubicacion = request.POST.get('ubicacion')
        requisitos = request.POST.get('requisitos')
        vacante = Vacante.objects.create(nombre_vacante = nom_vacante, descripcion = desc, disponibles = disp, salario = salario, ubicacion = ubicacion,requisitos = requisitos, empleador = request.user)
        vacante.save()
        generar_imagen(vacante)
    return redirect('image_gen', vacante_id = vacante.id)
@login_required(login_url='/login')
def home(request:HttpRequest):
    return render(request,'vacante.html')   
@login_required(login_url='/login')
def image_gen(request:HttpRequest,vacante_id:int):
    vacante = Vacante.objects.get(id = vacante_id)
    return render(request,'image_gen.html',{'vacante':vacante})
def login_(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

    context = {'loginform':form}    
    return render(request,'login.html', context=context)
def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            usuario = Usuario(user=user, profile_picture=request.FILES['profile_picture'])
            usuario.save()
            return redirect("/login")
        
    context = {'registerform' : form}

    return render(request,'signup.html', context=context)
def logout_(request):
    logout(request)
    return redirect("/")
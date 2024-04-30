from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpRequest
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import requests
from PIL import Image
from io import BytesIO
import numpy as np
from . forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Vacante
from magnetopostit.settings import MEDIA_ROOT

_ = load_dotenv('openAI.env')
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get('openAI_api_key'),
)

def fetch_image(url):
    response = requests.get(url)
    response.raise_for_status()

    # Convert the response content into a PIL Image
    image = Image.open(BytesIO(response.content))
    return(image)
def select_content(request,vac):
    vacante = Vacante.objects.get(id = vac)
    
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
    return redirect('select-content', vacante_id = vacante.id)
@login_required(login_url='/login')
def home(request:HttpRequest):
    return render(request,'vacante.html')   
def generar_imagen(vacante:Vacante):
        response = client.images.generate(
            model="dall-e-3",
            prompt=f"Imagen que respresente el trabajo de {vacante.nombre_vacante}",
            size="1024x1024",
            quality="standard",
            n=1,
            )
        image_url = response.data[0].url
        image = fetch_image(image_url)
        image.save(f'{MEDIA_ROOT}/images/{vacante.nombre_vacante}_id_{vacante.id}.jpg')
        vacante.imagen = f'images/{vacante.nombre_vacante}_id_{vacante.id}.jpg'
        vacante.save()
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
            form.save()
            return redirect("/login")
        
    context = {'registerform' : form}

    return render(request,'signup.html', context=context)
def logout_(request):
    logout(request)
    return redirect("/")
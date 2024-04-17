from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpRequest
import os
from openai import OpenAI
import json
from dotenv import load_dotenv, find_dotenv
import requests
from PIL import Image
from io import BytesIO
import numpy as np
from . forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.decorators import login_required
from .models import Vacante

# _ = load_dotenv('openAI.env')
# client = OpenAI(
#     # This is the default and can be omitted
#     api_key=os.environ.get('openAI_api_key'),
# )

# def fetch_image(url):
#     response = requests.get(url)
#     response.raise_for_status()

#     # Convert the response content into a PIL Image
#     image = Image.open(BytesIO(response.content))
#     return(image)

# Create your views here.
@login_required(login_url='/login')
def home(request:HttpRequest):
    return render(request,'vacante.html')   
def generar_imagen(request):
    if request.method == 'POST':
        nom_vacante = request.POST.get('nombre-vacante')
        desc = request.POST.get('descripcion')
        disp = request.POST.get('vacantes-disp')
        salario = request.POST.get('salario')
        ubicacion = request.POST.get('ubicacion')
        requisitos = request.POST.get('requisitos')
        # response = client.images.generate(
        #     model="dall-e-3",
        #     prompt=f"Imagen que respresente el trabajo de {nom_vacante}",
        #     size="1024x1024",
        #     quality="standard",
        #     n=1,
        #     )
        # image_url = response.data[0].url
        # print(image_url)
@login_required(login_url='/login')
def image_gen(request:HttpRequest):
    if request.method == 'POST':
        nom_vacante = request.POST.get('nombre-vacante')
        desc = request.POST.get('descripcion')
        disp = request.POST.get('vacantes-disp')
        salario = request.POST.get('salario')
        ubicacion = request.POST.get('ubicacion')
        requisitos = request.POST.get('requisitos')
        vacante = Vacante.objects.create(nombre_vacante = nom_vacante, descripcion = desc, disponibles = disp, salario = salario, ubicacion = ubicacion, empleador = request.user)
        vacante.save()
    return render(request,'image_gen.html',{'nombre':vacante.nombre_vacante,'desc':vacante.descripcion,'disp':vacante.descripcion,'salario':vacante.salario,'ubicacion':vacante.ubicacion,'requisitos':vacante.requisitos,'imagen':vacante.imagen})
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
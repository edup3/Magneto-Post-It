from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request,'vacante.html')
def image_gen(request):
    return render(request,'image_gen.html')
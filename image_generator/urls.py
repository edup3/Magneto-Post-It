from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('image/',views.image_gen,name='image_gen')
]
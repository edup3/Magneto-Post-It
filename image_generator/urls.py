from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('image/<int:vacante_id>',views.image_gen, name='image_gen'),
    path('login/', views.login_, name="login"),
    path('signup/',views.signup, name="signup"),
    path('logout/', views.logout_, name="logout"),
    path('procesando/',views.espera,name='espera'),
    path('cambiar_imagen/<int:vacante_id>',views.cambiar_imagen, name='cambiar_imagen')
]
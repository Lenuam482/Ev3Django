from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index,name='index'),
    path('darwin', views.darwin,name='darwin'),
    path('tortuga', views.tortuga,name='tortuga'),
    path('mapa', views.mapa,name='mapa'),
    path('mascotas', views.mascotas,name='mascotas'),
    path('agregar_al_carrito/<str:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),

]
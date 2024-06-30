from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index,name='index'),
    path('darwin', views.darwin,name='darwin'),
    path('tortuga', views.tortuga,name='tortuga'),
    path('mapa', views.mapa,name='mapa'),
    path('mascotas', views.mascotas,name='mascotas'),
    path('agregar_al_carro/', views.agregar_al_carro, name='agregar_al_carro'),
    path('', views.index, name='index'),
    path('compra', views.compra,name='compra'),
    path('eliminar_del_carrito/<str:nombre>', views.eliminar_del_carrito, name='eliminar_del_carro')

]
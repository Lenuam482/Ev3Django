from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('darwin', views.darwin, name='darwin'),
    path('tortuga', views.tortuga, name='tortuga'),
    path('mapa', views.mapa, name='mapa'),
    path('mascotas', views.mascotas, name='mascotas'),
    path('agregar_al_carro/', views.agregar_al_carro, name='agregar_al_carro'),
    path('', views.index, name='index'),
    path('compra', views.compra,name='compra'),
    path('eliminar_del_carro/<str:nombre>', views.eliminar_del_carro, name='eliminar_del_carro'),
    path('ad_productos/', views.ad_productos, name='ad_productos'),
    path('eliminar_producto/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('listar_producto', views.listar_producto, name='listar_producto'),
    path('edicion_producto/<int:pk>/', views.edicion_producto, name='edicion_producto'),
    path('productoupdate/<int:codigo>', views.productoupdate, name='productoupdate')

]
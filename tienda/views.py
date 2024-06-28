from django.shortcuts import render
from .models import Usuario, Producto, Carrito, CarritoProducto
# Create your views here.
def index(request):
    usuario = Usuario.objects.all()
    productos = Producto.objects.all()
    carrito = Carrito.objects.all()
    context={"usuario": usuario,
             "productos": productos,
             "carrito" : carrito}   
    return render(request,'tienda/index.html',context)

def darwin(request):
    usuario = Usuario.objects.all()
    productos = Producto.objects.all()
    carrito = Carrito.objects.all()
    context={"usuario": usuario,
             "productos": productos,
             "carrito" : carrito}
    return render(request,'tienda/darwin.html',context)

def mascotas(request):
    usuario = Usuario.objects.all()
    productos = Producto.objects.all()
    carrito = Carrito.objects.all()
    context={"usuario": usuario,
             "productos": productos,
             "carrito" : carrito}
    return render(request,'tienda/mascotas.html',context)

def tortuga(request):
    usuario = Usuario.objects.all()
    productos = Producto.objects.all()
    carrito = Carrito.objects.all()
    context={"usuario": usuario,
             "productos": productos,
             "carrito" : carrito}
    return render(request,'tienda/tortuga.html',context)

def mapa(request):
    usuario = Usuario.objects.all()
    productos = Producto.objects.all()
    carrito = Carrito.objects.all()
    context={"usuario": usuario,
             "productos": productos,
             "carrito" : carrito}
    return render(request,'tienda/mapa.html',context)

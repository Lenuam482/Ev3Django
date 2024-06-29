from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Producto, Carrito, CarritoProducto
from django.http import HttpResponse
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

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, codigo=producto_id)
    
    carrito = request.session.get('Carrito', {})
    if producto_id in carrito:
        carrito[producto_id]['cantidad'] += 1
    else:
        carrito[producto_id] = {
            'nombre': producto.nombre,
            'precio': producto.precio,
            'cantidad': 1
        }
    
    request.session['carrito'] = carrito
    return redirect('index')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Carrito, CarritoProducto
from django.http import HttpResponse
# Create your views here.
def index(request):
    productos = Producto.objects.all()
    carrito = Carrito.objects.all()
    context={
             "productos": productos,
             "carrito" : carrito}   
    return render(request,'tienda/index.html',context)

def darwin(request):
    
    productos = Producto.objects.all()
    carrito = Carrito.objects.all()
    context={
             "productos": productos,
             "carrito" : carrito}
    return render(request,'tienda/darwin.html',context)

def mascotas(request):
    
    productos = Producto.objects.all()
    carrito = Carrito.objects.all()
    context={
             "productos": productos,
             "carrito" : carrito}
    return render(request,'tienda/mascotas.html',context)

def tortuga(request):
    
    productos = Producto.objects.all()
    carrito = Carrito.objects.all()
    context={
             "productos": productos,
             "carrito" : carrito}
    return render(request,'tienda/tortuga.html',context)

def mapa(request):
    
    productos = Producto.objects.all()
    carrito = Carrito.objects.all()
    context={
             "productos": productos,
             "carrito" : carrito}
    return render(request,'tienda/mapa.html',context)

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, codigo=producto_id)

    # Obtén el carrito de la sesión o crea uno nuevo si no existe
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        carrito = get_object_or_404(Carrito, id=carrito_id)
    else:
        carrito = Carrito.objects.create()
        request.session['carrito_id'] = carrito.id

    carrito_producto, created = CarritoProducto.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        carrito_producto.cantidad += 1
        carrito_producto.save()

    return redirect('index')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Carro
from django.http import HttpResponse
from django.views.decorators.http import require_POST
# Create your views here.

def ad_productos(request):
    carro = Carro.objects.all()
    productos = Producto.objects.all()
    context={"productos": productos,
             "carro" : carro}   
    return render(request,'tienda/ad_productos.html',context)

def compra(request):
    carro = Carro.objects.all()
    productos = Producto.objects.all()
    context={"productos": productos,
             "carro" : carro}  
    return render(request,'tienda/compra.html',context)

def index(request):
    carro = Carro.objects.all()
    productos = Producto.objects.all()
    context={"productos": productos,
             "carro" : carro}   
    return render(request,'tienda/index.html',context)

def darwin(request):
    carro = Carro.objects.all()
    productos = Producto.objects.all()
    context={
             "productos": productos,
             "carro" : carro}
    return render(request,'tienda/darwin.html',context)

def mascotas(request):
    carro = Carro.objects.all()
    productos = Producto.objects.all()
    context={
             "productos": productos,
             "carro" : carro}
    return render(request,'tienda/mascotas.html',context)

def tortuga(request):
    carro = Carro.objects.all()
    productos = Producto.objects.all()
    context={
             "productos": productos,
             "carro" : carro}
    return render(request,'tienda/tortuga.html',context)

def mapa(request):
    carro = Carro.objects.all()
    productos = Producto.objects.all()
    context={
             "productos": productos,
             "carro" : carro}
    return render(request,'tienda/mapa.html',context)

def agregar_al_carro(request):

    nombre = request.POST['nombre']
    precio = request.POST['precio']
    
    producto_en_carro, created = Carro.objects.get_or_create(
        nombre=nombre,
        defaults={'precio': precio, 'cantidad': 1}
    )
    
    if not created:
        producto_en_carro.cantidad += 1
        producto_en_carro.save()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

def eliminar_del_carro(request, nombre):
    if request.method == 'POST':
        carro = get_object_or_404(Carro, nombre=nombre)
        carro.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))

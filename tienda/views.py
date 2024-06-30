from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Carro
from django.http import HttpResponse
from django.views.decorators.http import require_POST
# Create your views here.

def compra(request):
    carro = Carro.objects.all()
    productos = Producto.objects.all()
    context={"productos": productos,
             "carro" : carro}  
    return render(request,'tienda/compra.html',context)

def index(request):
    carro = Carro.objects.all()
    productos = Producto.objects.all()
    # carrito = Carrito.objects.all()
    # carritoProducto = CarritoProducto.objects.all()
    context={ #"carritoProducto" : carritoProducto,
             "productos": productos,
             "carro" : carro}
             #"carrito" : carrito}   
    return render(request,'tienda/index.html',context)

def darwin(request):
    carro = Carro.objects.all()
    productos = Producto.objects.all()
    #carrito = Carrito.objects.all()
    context={
             "productos": productos,
             "carro" : carro}
    return render(request,'tienda/darwin.html',context)

def mascotas(request):
    carro = Carro.objects.all()
    productos = Producto.objects.all()
    #carrito = Carrito.objects.all()
    context={
             "productos": productos,
             "carro" : carro}
    return render(request,'tienda/mascotas.html',context)

def tortuga(request):
    carro = Carro.objects.all()
    productos = Producto.objects.all()
    #carrito = Carrito.objects.all()
    context={
             "productos": productos,
             "carro" : carro}
    return render(request,'tienda/tortuga.html',context)

def mapa(request):
    carro = Carro.objects.all()
    productos = Producto.objects.all()
    #carrito = Carrito.objects.all()
    context={
             "productos": productos,
             "carro" : carro}
    return render(request,'tienda/mapa.html',context)

def agregar_al_carro(request):
    codigo = request.POST['codigo']
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

def eliminar_del_carrito(request, carrito_producto_id):
    carrito_producto = get_object_or_404(CarritoProducto, id=carrito_producto_id)
    
    # Elimina el producto del carrito
    carrito_producto.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))

# def agregar_al_carrito(request, producto_id):
#     producto = get_object_or_404(Producto, codigo=producto_id)

#     # Obtén el carrito de la sesión o crea uno nuevo si no existe
#     carrito_id = request.session.get('carrito_id')
#     if carrito_id:
#         try:
#             carrito = Carrito.objects.get(id=carrito_id)
#         except Carrito.DoesNotExist:
#             carrito = Carrito.objects.create()
#             request.session['carrito_id'] = carrito.id
#     else:
#         carrito = Carrito.objects.create()
#         request.session['carrito_id'] = carrito.id

#     carrito_producto, created = CarritoProducto.objects.get_or_create(carrito=carrito, producto=producto)
#     if not created:
#         carrito_producto.cantidad += 1
#         carrito_producto.save()

#     return redirect('index')  # Redirige a la vista principal o a donde desees

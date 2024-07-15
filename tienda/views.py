from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Carro
from .forms import ProductoForm
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

def listar_producto(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda/listar_producto.html', context)


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

def eliminar_producto(request,pk):
    context={}
    try:
        producto=Producto.objects.get(codigo=pk)
        producto.delete()
        mensaje="Producto Eliminado"
        productos = Producto.objects.all()
        context = {'productos':productos, 'mensaje':mensaje}
        return render(request, 'tienda/listar_producto.html', context)
    except:
        mensaje="Error, producto no existe"
        productos = Producto.objects.all()
        context = {'productos':productos, 'mensaje':mensaje}
        return render(request, 'tienda/listar_producto.html', context)

def ad_productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ad_productos')
    else:
        form = ProductoForm()
    return render(request, 'tienda/ad_productos.html', {'form': form})

def edicion_producto(request, pk):
    if pk != "":
        productos=Producto.objects.get(codigo=pk)
        context={"productos": productos}

        if productos:
            return render(request, 'tienda/edicion_producto.html', context)
        else:
            context={'mensaje':"Error, nombre producto no existe"}
            return render(request, 'tienda/edicion_producto.html', context)
        
def productoupdate(request, codigo):
    try:

        nombre=request.POST["nombre"]
        precio=request.POST["precio"]
        descripcion=request.POST["descripcion"]
        

        productos = Producto.objects.get(codigo = codigo)
        
        
        try:
            imagen = request.FILES['imagen']
            ruta_foto = "media/"+str(productos.imagen)
            import os 
            if ruta_foto != "media/productos/noimagen.jpg":
                os.remove(ruta_foto)
        except:
            imagen = productos.imagen

        productos.nombre=nombre
        productos.precio=precio
        productos.descripcion=descripcion
        productos.imagen=imagen
                
        productos.save
        productos = Producto.objects.all().values()
        context={'mensaje':"Ok, producto actualizado",'productos': productos}
        return render(request, 'tienda/listar_producto.html', context)
    except:
        productos = Producto.objects.all().values()
        context={'mensaje':"Error al actualizar producto",'productos': productos}
        return render(request, 'tienda/listar_producto.html', context)
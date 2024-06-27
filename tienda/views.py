from django.shortcuts import render
from .models import Usuario
# Create your views here.
def index(request):
    usuario = Usuario.objects.all()
    context={"usuario": usuario}
    return render(request,'tienda/index.html',context)

def darwin(request):
    usuario = Usuario.objects.all()
    context={"usuario": usuario}
    return render(request,'tienda/darwin.html',context)

def mascotas(request):
    usuario = Usuario.objects.all()
    context={"usuario": usuario}
    return render(request,'tienda/mascotas.html',context)

def tortuga(request):
    usuario = Usuario.objects.all()
    context={"usuario": usuario}
    return render(request,'tienda/tortuga.html',context)

def mapa(request):
    usuario = Usuario.objects.all()
    context={"usuario": usuario}
    return render(request,'tienda/mapa.html',context)

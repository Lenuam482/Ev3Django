from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'tienda/index.html',context)

def darwin(request):
    context={}
    return render(request,'tienda/darwin.html',context)

def mascotas(request):
    context={}
    return render(request,'tienda/mascotas.html',context)

def tortuga(request):
    context={}
    return render(request,'tienda/tortuga.html',context)

def mapa(request):
    context={}
    return render(request,'tienda/mapa.html',context)
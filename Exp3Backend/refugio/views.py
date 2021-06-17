from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def Index(request):
    return render(request, 'Index.html')


def Galeria_de_fotos(request):

    return render(request, 'Galeria_de_fotos.html')


def form_ver(request):
    productos = Producto.objects.all()
    return render(request, 'refugio/form_ver.html', {'productos':productos})

def form_crear(request):
    if request.method=='POST': 
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('form_ver')
    else:
       producto_form= ProductoForm()
    return render(request, 'refugio/form_crear.html', {'producto_form': producto_form})

def form_modificar(request,id):
    producto = Producto.objects.get(idProducto=id)

    datos ={
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST': 
        formulario = ProductoForm(data=request.POST, instance = producto)
        if formulario.is_valid: 
            formulario.save()
            return redirect('form_ver')
    return render(request, 'refugio/form_modificar.html', datos)

def form_eliminar(request,id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect('form_ver')
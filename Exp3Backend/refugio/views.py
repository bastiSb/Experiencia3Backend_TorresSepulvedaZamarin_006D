from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, 'Index.html')

def Galeria_de_fotos(request):
    return render(request, 'Galeria_de_fotos.html')
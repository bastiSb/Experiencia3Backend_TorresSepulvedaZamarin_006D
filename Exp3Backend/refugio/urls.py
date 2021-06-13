from django.urls import path
from .views import Index,Galeria_de_fotos

urlpatterns = [
    path('', Index,name="Index"),
    path('Galeria_de_fotos', Galeria_de_fotos,name="Galeria_de_fotos"),
]

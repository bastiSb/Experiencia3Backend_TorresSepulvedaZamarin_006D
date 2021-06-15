from django.urls import path
from .views import Galeria_de_fotos, Index, form_ver, form_crear, form_modificar,form_eliminar

urlpatterns = [
    path('', Index,name="Index"),
    path('Galeria_de_fotos', Galeria_de_fotos,name="Galeria_de_fotos"),
    path('form_ver', form_ver, name="form_ver"),
    path('form_crear', form_crear, name="form_crear"),
    path('form_modificar/<id>', form_modificar, name="form_modificar"),
    path('form_eliminar/<id>', form_eliminar, name="form_eliminar"),
]
from django import forms
from django.forms import ModelForm
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Producto



class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto', 'precioProducto', 'cantProducto',
        'categoria']
        labels ={
            'idProducto': 'codigo', 
            'nombreProducto': 'nombre', 
            'precioProducto': 'precio', 
            'cantProducto': 'cantidad',
            'categoria': 'Categoria',
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese codigo', 
                    'id': 'idProducto'
                }
            ), 
            'nombreProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombreProducto'
                }
            ), 
            'precioProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese precio', 
                    'id': 'precioProducto'
                }
            ), 
            'cantProducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'cantProducto',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }

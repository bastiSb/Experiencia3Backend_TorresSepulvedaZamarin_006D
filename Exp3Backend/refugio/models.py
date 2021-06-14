from django.db import models

# Create your models here.

class Categoria (models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria =models.CharField(max_length=25,verbose_name='Nombre de categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto (models.Model):
    idProducto =models.IntegerField(primary_key=True, verbose_name='Id de producto')
    nombreProducto =models.CharField(max_length=25,verbose_name='Nombre de producto')
    precioProducto =models.IntegerField(verbose_name='Precio de producto')
    cantProducto =models.IntegerField(verbose_name='Cantidad de producto')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreProducto
        
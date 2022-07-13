from tabnanny import verbose
from tkinter import commondialog
from django.db import models

class Usuarios(models.Model):
    username = models.CharField(max_length=30,primary_key=True, verbose_name='Nombre de usuario')
    mail = models.CharField(max_length=60, null=False, blank=False,unique=True, verbose_name='Correo')
    password = models.CharField(max_length=60, null=False, blank=False, verbose_name='Contraseña')
    suscripcion = models.BooleanField(verbose_name=('membresia'), default=False)
    class Meta:
        verbose_name_plural = 'Usuarios'
    def __str__(self):
        return self.username
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        del self

class FormSolicitud(models.Model):
    idSolicitud = models.AutoField(primary_key=True, verbose_name='Id solicitud')
    nombreCompleto = models.CharField(max_length=60, null=False, verbose_name='Nombre completo')
    mailSolicitante = models.CharField(max_length=60, null=False, verbose_name='Mail del solicitate')
    descripcion = models.CharField(max_length=1000, null=False, verbose_name='Descripcion')
   
    class Meta:
        verbose_name_plural = 'FormSolicitud'
    def __str__(self):
        return self.nombreCompleto

class CategoriaProduct(models.Model):
    idCategoria = models.IntegerField(primary_key=True,null=False, blank=False, verbose_name='Id categoria')
    nombreCategoria = models.CharField(max_length=40 ,unique=True, null=False, blank=False, verbose_name='Nombre categoria')
    class Meta:
        verbose_name_plural = 'CategoriaProduct'
    def __str__(self):
        return self.nombreCategoria

class CatalogoProduct(models.Model):
    idProduct = models.AutoField(primary_key=True, verbose_name='Id Producto')
    nombreProducto = models.CharField(max_length=30, null=False, blank=False, unique=True, verbose_name='Nombre Producto')
    descripcionProducto = models.CharField(max_length=500, null=False, blank=True, verbose_name='Descripcion Producto')
    precioProducto  = models.IntegerField(null=False,blank=False, verbose_name='Precio Producto')
    categoria =  models.ForeignKey(CategoriaProduct, on_delete=models.CASCADE)
    imagenProducto = models.CharField(max_length=2000, verbose_name='url foto del Producto')   
    stockProducto = models.IntegerField(null=False, blank=False, verbose_name='Stock Producto')
    class Meta:
        verbose_name_plural = 'CatalogoProduct'
    def __str__(self):
        return self.nombreProducto

class boleta(models.Model):
    idBoleta = models.AutoField(primary_key=True, verbose_name='Numero boleta')
    precioTotal = models.IntegerField(null=False, blank=False, verbose_name='Precio total')
    fecha = models.DateField(verbose_name='Fecha boleta')

    def __str__(self):
        return str(self.idBoleta)
class Descuento(models.Model):
    IdCodigo= models.CharField(max_length=30,primary_key=True,verbose_name='Id Codigo')
    Porcentaje= models.IntegerField(null=False,blank=False,verbose_name='Porcentaje Descuento')

    def __str__(self):
        return str(self.IdCodigo)
## Create your models here.


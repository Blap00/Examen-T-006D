from attr import fields
from rest_framework import serializers
from core.models import *

class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = ['IdCodigo','Porcentaje']

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = boleta
        fields = ['idBoleta','precioTotal','fecha']
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuarios
        fields = '__all__'
        

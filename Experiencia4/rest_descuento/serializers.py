from rest_framework import serializers
from core.models import Descuento, boleta

class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = ['IdCodigo','Porcentaje']

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = boleta
        fields = ['idBoleta','precioTotal','fecha']

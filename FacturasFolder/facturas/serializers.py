from rest_framework import serializers
from . import models


class FacturaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'nombre', 'monto','metodo' ,'documento_identidad')
        model = models.Factura
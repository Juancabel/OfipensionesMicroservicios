from django.db import models
from pgcrypto import fields

class Factura(models.Model):
    nombre = fields.TextPGPSymmetricKeyField(max_length=50, verbose_name='nombre')
    monto = fields.FloatPGPSymmetricKeyField(default =None,null=True,blank=True, verbose_name='monto')
    metodo = fields.TextPGPSymmetricKeyField(max_length=20, verbose_name='metodo')
    documento_identidad = fields.TextPGPSymmetricKeyField(max_length=10, verbose_name='documento_identidad')


    def __str__(self):
        return '%s %s' % (self.nombre, self.documento_identidad,self.metodo)
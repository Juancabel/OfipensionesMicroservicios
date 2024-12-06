from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('facturas/', views.facturas_list, name='facturaList'),
    path('facturacreate/', csrf_exempt(views.crear_factura), name='facturaCreate'),
]
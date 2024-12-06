from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import FacturaForm
from .logic.facturas_logic import get_facturas, create_factura
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import FacturaSerializer
from django.contrib.auth.decorators import login_required
from ofipensiones.auth0backend import getRole
import json

@login_required
def facturas_list(request):
    role = getRole(request)
    if role != "Administrador":
        return HttpResponse("Unauthorized User")
    facturas = get_facturas()
    serializer = FacturaSerializer(facturas,many=True)
    context = {
        'factura_list': serializer.data
    }
    return render(request, 'facturas/facturas.html', context)


def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            create_factura(form)
            messages.add_message(request, messages.SUCCESS, 'Factura creada exitosamente')
            return HttpResponseRedirect(reverse('facturaCreate'))
        else:
            print(form.errors)
    else:
        form = FacturaForm()
    context = {
        'form': form,
    }
    return render(request, 'facturas/facturaCreate.html', context)

    
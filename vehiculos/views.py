from django.shortcuts import render
from django.http import HttpResponse
from . models import Carro
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    carros = Carro.objects.all()
    return render(request, 'index.html', {'carros': carros})

class ModificarVehiculo(UpdateView):
    model = Carro
    template_name = 'editar_vehiculo.html'
    success_url = reverse_lazy('vehiculos:index')
    fields = ['marca', 'modelo', 'precio', 'image']

class EliminarVehiculo(DeleteView):
    model = Carro
    template_name = 'eliminar_vehiculo.html'
    success_url = reverse_lazy('vehiculos:index')

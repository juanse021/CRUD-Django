from django.shortcuts import render
from django.http import HttpResponse
from . models import Carro
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

class IndexVehiculo(ListView):
    template_name = 'index.html'
    queryset = Carro.objects.all()
    context_object_name = 'carros'

class ModificarVehiculo(UpdateView):
    model = Carro
    template_name = 'editar_vehiculo.html'
    success_url = reverse_lazy('vehiculos:index')
    fields = ['marca', 'modelo', 'precio', 'image']

class EliminarVehiculo(DeleteView):
    model = Carro
    template_name = 'eliminar_vehiculo.html'
    success_url = reverse_lazy('vehiculos:index')

class CrearVehiculo(CreateView):
    model = Carro
    template_name = 'crear_vehiculo.html'
    success_url = reverse_lazy('vehiculos:index')
    fields = ['marca', 'modelo', 'precio', 'image']

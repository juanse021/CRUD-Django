from django.urls import path

from . import views

app_name = "vehiculos"
urlpatterns = [
    path('', views.index, name='index'),
    path('editar/<int:pk>/', views.ModificarVehiculo.as_view(), name="editar-vehiculo"),
    path('eliminar/<int:pk>/', views.EliminarVehiculo.as_view(), name="eliminar-vehiculo")
]
from django.urls import path

from . import views

app_name = "vehiculos"
urlpatterns = [
    path('', views.IndexVehiculo.as_view(), name='index-vehiculo'),
    path('editar/<int:pk>/', views.ModificarVehiculo.as_view(), name="editar-vehiculo"),
    path('eliminar/<int:pk>/', views.EliminarVehiculo.as_view(), name="eliminar-vehiculo"),
    path('nuevo/', views.CrearVehiculo.as_view(), name="crear-vehiculo")
]
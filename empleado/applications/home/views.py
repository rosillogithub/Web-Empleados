from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Prueba

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/home.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html' # muestra el resultado del proceso (común para el uso de todas las vistas genericas)
    queryset = ['A','B','C']  # Que se va a listar. Podria ser una funcion que consulte una BD
    context_object_name = "lista_prueba" # Agrega variable

class ModeloPruebaListView(ListView):
    model = Prueba      # importar la clase Prueba desde models
    template_name = "home/pruebas.html"
    context_object_name = "lista_prueba"

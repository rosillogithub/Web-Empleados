from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/home.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html' # muestra el resultado del proceso (común para el uso de todas las vistas genericas)
    queryset = ['A','B','C']  # Que se va a listar. Podria ser una funcion que consulte una BD
    context_object_name = "lista_prueba" # Agrega variable
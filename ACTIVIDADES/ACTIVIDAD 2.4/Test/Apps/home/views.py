from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
    template_name='index.html' 

class CreditosView(TemplateView):
    template_name='creditos.html'

class estudiantesView(TemplateView):
    template_name='estudiantes.html'

class administradoresView(TemplateView):
    template_name='administradores.html'

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Admins, Articulos, Cliente, Estudiantes
from django .forms import forms
from .forms import FormAdmins, FormArticulos, FormEstudiante
from  django.forms import forms
from django.urls import reverse_lazy
# Create your views here.
class HomeView(TemplateView):
    template_name='index.html' 

class CreditosView(TemplateView):
    template_name='creditos.html' 
    

class estudiantesView(CreateView):
    model= Estudiantes
    form_class=FormEstudiante
    template_name='estudiantes.html'
    success_url=reverse_lazy('jesus:estudiantes')

class administradoresView(CreateView):
    model= Admins
    form_class=FormAdmins
    template_name='administradores.html'
    success_url=reverse_lazy('jesus:administradores')

class ListarCliente(ListView):
    template_name = 'Listar_cli.html'
    model = Estudiantes

    def get_queryset(self):
        return Estudiantes.objects.all()

class ListarAdmins(ListView):
    template_name = 'Listar_admin.html'
    model = Admins

    def get_queryset(self):
        return Admins.objects.all()

class ListarArticulos(ListView):
    template_name = 'Listar_Articulos.html'
    model = Articulos

    def get_queryset(self):
        return Articulos.objects.all()
        
        # return Cliente.objects.filter(nombre = 'carlos')


from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import Admins, Articulos, Estudiantes

class FormEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields=[
            'nombre',
            'apellido',
            'direccion',
            'carne',
        ]
        labels={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'direccion':'Direccion', 
            'carne':'Carne',
        }

class FormAdmins(forms.ModelForm):
    class Meta:
        model = Admins
        fields=[
            'nombre',
            'apellido',
            'direccion',
            'carne',
        ]
        labels={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'direccion':'Direccion', 
            'carne':'Carne',
        }    

class FormArticulos(forms.ModelForm):
    class Meta:
        model = Articulos
        fields=[
            'titulo',
            'contenido',
            'fecha',
            
        ]
        labels={
            'titulo':'Titulo',
            'contenido':'Contenido',
            'fecha':'Fecha', 
      
        }   
from Apps.home.models import Cliente
from django.contrib import admin
from .models import Admins, Articulos, Cliente, Comentarios, Estudiantes, TipoCliente

# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoCliente)
admin.site.register(Estudiantes)
admin.site.register(Admins)
admin.site.register(Comentarios)
admin.site.register(Articulos)



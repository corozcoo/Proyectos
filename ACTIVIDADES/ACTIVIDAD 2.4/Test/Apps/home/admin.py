from Apps.home.models import Cliente
from django.contrib import admin
from .models import Cliente, TipoCliente

# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoCliente)

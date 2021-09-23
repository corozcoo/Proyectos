"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .views import ListarComentarios, articulosView, HomeView, ListarAdmins, ListarArticulos, administradoresView, ComentariosView, estudiantesView, ListarCliente

app_name = 'jesus'

urlpatterns = [

    path('index/', HomeView.as_view(), name='home'),
    path('articulos/', articulosView.as_view(), name='articulos'),
    path('administradores/', administradoresView.as_view(), name='administradores'),
    path('estudiantes/', estudiantesView.as_view(), name='estudiantes'),
    path('Listarcli/', ListarCliente.as_view(), name='Listar_cli'),
    path('Listaradmins/', ListarAdmins.as_view(), name='Listar_admins'),
    path('ListarArticulos/', ListarArticulos.as_view(), name='Listar_Articulos'),
    path('Comentarios/', ComentariosView.as_view(), name='Comentarios'),
    path('ListarComentarios/', ListarComentarios.as_view(), name='Listar_Comentarios'),

]

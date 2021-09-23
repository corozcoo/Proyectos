from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Cliente(models.Model):
    doc = {
        ('D','DPI'),
        ('C','CEDULA'),
 
    } 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    nacimiento = models.DateField()
    tipo = models.ForeignKey(
        'TipoCliente',
        on_delete= models.CASCADE,
        default=1
        )
    documento = models.CharField(
        max_length=20,
        choices=doc,
        default='C')
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class TipoCliente(models.Model):
    tipo = models.CharField(max_length=10)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.tipo)

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    carne = models.CharField(max_length=200)
    
    def __str__(self):
        return '%s' % (self.nombre)

class Admins(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    carne = models.CharField(max_length=200)
    
    
    def __str__(self):
        return '%s' % (self.nombre)

        
class Comentarios(models.Model):
    contenido = models.CharField(max_length=500)
    fecha = models.DateTimeField()
    Articulos = models.ForeignKey(
        'Articulos',
        on_delete= models.CASCADE,
        default=1
        )
    Estudiantes = models.ForeignKey(
        'Estudiantes',
        on_delete= models.CASCADE,
        default=1
        )
    
    def __str__(self):
        return '%s' % (self.contenido) 


class Articulos(models.Model):
    titulo = models.CharField(max_length=20)
    contenido = models.CharField(max_length=500)
    fecha = models.DateTimeField()
    Estudiantes = models.ForeignKey(
        'Estudiantes',
        on_delete= models.CASCADE,
        default=1
        )
    Admins = models.ForeignKey(
        'Admins',
        on_delete= models.CASCADE,
        default=1
        )

    def __str__(self):
        return '%s' % (self.contenido)  

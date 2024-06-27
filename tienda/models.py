from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(primary_key=True, max_length=10)
    clave = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.username)
    
class carrito(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField
    cantidad = models.IntegerField
    

class producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField
    imagen = models.ImageField(upload_to='productos/', default='media/default.png')
    descripcion = models.TextField()
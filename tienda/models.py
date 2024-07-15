from django.db import models

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True, verbose_name="Código")
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', default='productos/default.png')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Carro(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    cantidad = models.IntegerField()



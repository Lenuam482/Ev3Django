from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(primary_key=True, max_length=10)
    clave = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.username)
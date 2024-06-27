from django.db import models

class Usuario(models.Model):
    id_cliente = models.AutoField(db_column='idUsuario', primary_key=True)
    username = models.CharField(max_length=10)
    clave = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', default='productos/default.png')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    id_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='idUsuario')
    productos = models.ManyToManyField(Producto, through='CarritoProducto')

    def __str__(self):
        return f'Carrito de {self.id_cliente.username}'

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} en el carrito de {self.carrito.id_cliente.username}'

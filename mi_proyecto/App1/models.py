from django.db import models

# Create your models here.
class Cliente(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Correo = models.EmailField(max_length=254)
    TipoCliente = models.CharField(max_length=3)
    
    def __str__(self):
        Mostrar = self.Nombre + ' - ' + self.TipoClientes
        return Mostrar


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mensaje = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre} - {self.email}'
from django.db import models
from django.contrib.auth.models import User

class Id_Tanques(models.Model):
    id_tanque = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.id_tanque}"

class Tanques(models.Model):
    id_tanque = models.CharField(max_length=10)
    fecha = models.DateField()
    variedad = models.CharField(max_length=40)
    t = models.FloatField()
    brix = models.FloatField()
    ph = models.FloatField()
    cliente = models.CharField(max_length=30)
    enologo = models.CharField(max_length=30)
    observaciones = models.TextField(null=True)
    def __str__(self) -> str:
        return f"{self.id_tanque} - {self.fecha} - {self.variedad} - {self.t} - {self.brix} - {self.ph} - {self.cliente} - {self.enologo} - {self.observaciones}"

class MostoVino(models.Model):
    variedad = models.CharField(max_length=30)
    def __str__(self) -> str:
        return f"{self.variedad}"

class Clientes(models.Model):
    cliente = models.CharField(max_length=30)
    contacto = models.EmailField()
    def __str__(self) -> str:
        return f"{self.cliente} - {self.contacto}"

class Enologos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    telefono = models.IntegerField()
    puesto = models.CharField(max_length=30)
    tipo_contrato = models.CharField(max_length=30) 
    
    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} - {self.puesto} - {self.tipo_contrato}"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"

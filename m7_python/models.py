from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

class Tipo_inmueble(models.Model):
    tipo_inmueble = models.TextField()

class Comuna(models.Model):
    comuna = models.TextField()

class Region(models.Model):
    region = models.TextField()

class Tipo_user(models.Model):
    tipo_user = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.TextField()
    id_tipo_user = models.IntegerField(default=0)
    direccion = models.TextField()
    telefono = models.TextField()
    correo = models.TextField()

class Inmuebles(models.Model):
    id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    id_tipo_inmueble = models.ForeignKey('m7_python.Tipo_inmueble', on_delete=models.CASCADE, null=True)
    id_comuna = models.ForeignKey('m7_python.Comuna', on_delete=models.CASCADE, null=True)
    id_region = models.ForeignKey('m7_python.Region', on_delete=models.CASCADE, null=True)
    nombre_inmueble = models.TextField()
    descripcion = models.CharField(max_length=200)
    m2_construido = models.FloatField()
    numero_banos = models.IntegerField(default=0)
    numero_hab = models.IntegerField(default=0)
    direccion = models.CharField(max_length=200)
    # agregado. datos faltantes
    m2_terreno = models.FloatField(default=0.0) #fijarse que se agregó valor predeterminado
    numero_est = models.IntegerField(default=0)

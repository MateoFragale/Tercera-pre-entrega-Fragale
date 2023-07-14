from django.db import models

class Clase1(models.Model):
    pellido  = models.CharField(max_length=50)
    Edad = models.IntegerField()
    # Agrega más campos según tus necesidades
    
class Clase2(models.Model):
    Correo_electronico = models.CharField(max_length=50)
    Dia_de_nacimiento = models.IntegerField()
    # Agrega más campos según tus necesidades
    
class Clase3(models.Model):
    Mes_de_nacimiento = models.IntegerField()
    Año_de_nacimiento = models.IntegerField()
    # Agrega más campos según tus necesidades

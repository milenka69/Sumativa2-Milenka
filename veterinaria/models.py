from django.db import models

class Cliente (models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=150)
    numero_telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Atencion (models.Model):
    fecha = models.DateTimeField()
    nombre_mascota = models.CharField(max_length=100)
    tipo_animal = models.CharField(max_length=100)
    costo = models.PositiveIntegerField()
    dueño = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='atenciones',
    )
    
    def __str__(self):
        return self.nombre_mascota

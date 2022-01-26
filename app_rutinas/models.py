from django.db.models import Model
from django.db.models.fields import CharField, IntegerField, DateField

# Create your models here.

class Rutina(Model):

    nombre = CharField(max_length=40)
    fecha_inicio = DateField()
    intensidad = CharField(max_length=10)
    ejercicio_1 = CharField(max_length=40)
    ejercicio_2 = CharField(max_length=40)
    ejercicio_3 = CharField(max_length=40)
    ejercicio_4 = CharField(max_length=40)
    ejercicio_5 = CharField(max_length=40)
    ejercicio_6 = CharField(max_length=40)
    ejercicio_7 = CharField(max_length=40)
    duracionPorEjercicio = IntegerField()
    descansoEntreEjercicio = IntegerField()
    rondas = IntegerField()

    def __str__(self):
        return f'Rutina: {self.nombre} Intensidad: {self.intensidad} Ejercicio 1: {self.ejercicio_1}'
from django.db.models import Model
from django.db.models.fields import CharField, IntegerField, EmailField, DateField

# Create your models here.

class Atleta(Model):

    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    disciplina = CharField(max_length=40)
    fecha_nacimiento = DateField()
    ciudad_de_nacimiento = CharField(max_length=30)
    pais_de_nacimiento = CharField(max_length=30)
    altura = IntegerField()
    peso = IntegerField()
    email = EmailField()

    def __str__(self):
        return f'Atleta: {self.nombre} {self.apellido} Disciplina: {self.disciplina} Altura: {self.altura} Peso: {self.peso} Pais de origen: {self.pais_de_nacimiento} Email: {self.email}'
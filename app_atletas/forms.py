from django.forms import Form, IntegerField, CharField, EmailField, FloatField

class atleta_create(Form):
    nombre = CharField(max_length=30)
    apellido = CharField()
    disciplina = CharField()
    fecha_nacimiento = CharField()
    ciudad_de_nacimiento = CharField()
    pais_de_nacimiento = CharField()
    altura = IntegerField()
    peso = IntegerField()
    email = EmailField()
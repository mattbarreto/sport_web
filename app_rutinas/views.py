import email
from unittest import result
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app_rutinas.models import Rutina
from app_rutinas.forms import rutinas_create
from django.forms import model_to_dict

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


def inicio(request):

    return render(request, 'inicio.html')


def atleta(request):

    return render(request, 'atletas.html', 
    {'lista_atletas': Atleta.objects.all()})


def entrenador(request):

    return render(request, 'entrenadores.html')


def rutina_alta(request):
    if request.method == 'POST':
        formulario_rutinas = rutinas_create(request.POST)

        if formulario_rutinas.is_valid():
            data = formulario_rutinas.cleaned_data

            Rutina.objects.create(
                nombre=data['nombre'],
                fecha_inicio=data['fecha de inicio'],
                intensidad=data['intensidad'],
                ejercicio_1=data['ejercicio 1'],
                ejercicio_2=data['ejercicio 2'],
                ejercicio_3=data['ejercicio 3'],
                ejercicio_4=data['ejercicio 4'],
                ejercicio_5=data['ejercicio 5'],
                ejercicio_6=data['ejercicio 6'],
                ejercicio_7=data['ejercicio 7'],
                duracionPorEjercicio=data['duración por ejercicio'],
                descansoEntreEjercicio=data['descanso entre ejercicio'],
                rondas=data['rondas'],
            )
            return redirect('Rutinas')
    else:
        formulario_rutinas = rutinas_create()

    return render(request, 'rutinas_form.html', {'formulario_at': formulario_rutinas})


def rutinas_delete(request, id_rutinas):

    rutina = Rutina.objects.get(id=id_rutinas)
    rutina.delete()
    return redirect('Rutinas')


def rutina_update(request, id_rutinas):
    rutina = Rutina.objects.get(id=id_rutinas)

    if request.method == 'POST':
        formulario_rutinas = rutinas_create(request.POST)

        if formulario_rutinas.is_valid():
            data = formulario_rutinas.cleaned_data

            rutina.nombre = data['nombre'],
            rutina.fecha_inicio = data['fecha de inicio'],
            rutina.intensidad = data['intensidad'],
            rutina.ejercicio_1 = data['ejercicio 1'],
            rutina.ejercicio_2 = data['ejercicio 2'],
            rutina.ejercicio_3 = data['ejercicio 3'],
            rutina.ejercicio_4 = data['ejercicio 4'],
            rutina.ejercicio_5 = data['ejercicio 5'],
            rutina.ejercicio_6 = data['ejercicio 6'],
            rutina. ejercicio_7 = data['ejercicio 7'],
            rutina.duracionPorEjercicio = data['duración por ejercicio'],
            rutina.descansoEntreEjercicio = data['descanso entre ejercicio'],
            rutina.rondas = data['rondas'],

            rutina.save()

            return redirect('Rutinas')

    else:
        formulario_rutinas = rutinas_create(model_to_dict(rutina))

    return render(request, 'rutinas_form.html', {'formulario_at': formulario_rutinas})


def rutinas_busqueda(request):

    return render(request, 'rutinas_busqueda.html')


def buscar_rutina(request):

    if request.GET["nom"]:

        rut = request.GET["nom"]

        ruti = Rutina.objects.filter(nombre__icontains=rut)
        return render(request, "busqueda_rutinas.html", {"ruti": ruti, "query": rut})

    else:
        mensaje = "Por favor, introduzca un nombre para comenzar la búsqueda"

    return HttpResponse(mensaje)


class RutinasListView(ListView):
    model = Rutina
    template_name = 'rutinas.html'
    context_object_name = 'lista_rutinas'


class RutinasDetailView(DetailView):
    model = Rutina
    template_name = 'rutinas_ver.html'


class RutinasCreateView(CreateView):
    model = Rutina
    success_url = reverse_lazy('Rutinas')
    fields = ['nombre', 'fecha_inicio', 'intensidad', 'ejercicio_1', 'ejercicio_2', 'ejercicio_3', 'ejercicio_4', 'ejercicio_5', 'ejercicio_6', 'ejercicio_7', 'duracionPorEjercicio', 'descansoEntreEjercicio', 'rondas']
    template_name = 'rutinas_formulario.html'


class RutinasUpdateView(UpdateView):
    model = Rutina
    success_url = reverse_lazy('Rutinas')
    fields = ['nombre', 'fecha_inicio', 'intensidad', 'ejercicio_1', 'ejercicio_2', 'ejercicio_3', 'ejercicio_4', 'ejercicio_5', 'ejercicio_6', 'ejercicio_7', 'duracionPorEjercicio', 'descansoEntreEjercicio', 'rondas']
    template_name = 'rutinas_formulario.html'


class RutinasDeleteView(DeleteView):
    model = Rutina
    success_url = reverse_lazy('Rutinas')
    template_name = 'rutinas_confirm_delete.html'
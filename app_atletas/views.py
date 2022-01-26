from dataclasses import field
import email
from pyexpat import model
from re import template
from unittest import result
from winreg import DeleteValue
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app_atletas.models import Atleta
from app_atletas.forms import atleta_create

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


def rutina(request):

    return render(request, 'rutinas.html')


def atleta_alta(request):

    if request.method == 'POST':
        formulario_atletas = atleta_create(request.POST)

        if formulario_atletas.is_valid():
            data = formulario_atletas.cleaned_data

            Atleta.objects.create(
                nombre=data['nombre'],
                apellido=data['apellido'],
                edad=data['edad'],
                altura=data['altura'],
                peso=data['peso'],
                email=data['email']
            )
            return redirect('Atletas')
    else:
        formulario_atletas = atleta_create()

    return render(request, 'atletas_form.html', {'formulario_at': formulario_atletas})


def atleta_delete(request, id_atleta):

    atleta = Atleta.objects.get(id=id_atleta)
    atleta.delete()
    return redirect('Atletas')


def atleta_update(request, id_atleta):
    atleta = Atleta.objects.get(id=id_atleta)

    if request.method == 'POST':
        formulario_atletas = atleta_create(request.POST)

        if formulario_atletas.is_valid():
            data = formulario_atletas.cleaned_data

            atleta.nombre = data['nombre']
            atleta.apellido = data['apellido']
            atleta.edad = data['edad']
            atleta.altura = data['altura']
            atleta.peso = data['peso']
            atleta.email = data['email']

            atleta.save()

            return redirect('Atletas')

    else:
        formulario_atletas = atleta_create(model_to_dict(atleta))

    return render(request, 'atletas_form.html', {'formulario_at': formulario_atletas})


def atleta_busqueda(request):

    return render(request, 'atletas_busqueda.html')


def buscar(request):

    respuesta = f"El resultado de su busqueda es: {request.GET['nombre']} {request.GET['apellido']}"
    return HttpResponse(respuesta)


class atletaListView(ListView):
    model = Atleta
    template_name = 'atletas.html'
    context_object_name = 'lista_atletas'


class atletaDetailView(DetailView):
    model = Atleta
    template_name = 'atletas_ver.html'


class atletaCreateView(CreateView):
    model = Atleta
    success_url = reverse_lazy('Atletas')
    fields = ['nombre', 'apellido', 'disciplina', 'fecha_nacimiento',
    'ciudad_de_nacimiento', 'pais_de_nacimiento', 'altura', 'peso', 'email']
    template_name = 'atletas_formulario.html'


class atletaUpdateView(UpdateView):
    model = Atleta
    success_url = reverse_lazy('Atletas')
    fields = ['nombre', 'apellido', 'disciplina', 'fecha_nacimiento',
    'ciudad_de_nacimiento', 'pais_de_nacimiento', 'altura', 'peso', 'email']
    template_name = 'atletas_formulario.html'


class atletaDeleteView(DeleteView):
    model = Atleta
    success_url = reverse_lazy('Atletas')
    template_name = 'atletas_confirm_delete.html'
from django.urls import path
from app_rutinas.views import RutinasCreateView, RutinasDeleteView, RutinasDetailView, RutinasListView, RutinasUpdateView, buscar_rutina, inicio, rutinas_busqueda, Rutina
from app_atletas.views import atleta, atleta_busqueda, buscar
from app_entrenadores.views import entrenador

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('atletas', atleta, name='Atletas'),
    path('entrenadores', entrenador, name='Entrenadores'),
    path('buscarAtleta', atleta_busqueda, name='Busqueda de Atletas'),
    
    # A continuacion los paths especificos de esta app:
    
    path('buscar', buscar, name='Buscar'),
    path('rutinas', RutinasListView.as_view(), name='Rutinas'),
    path('rutinas/detalle/<pk>', RutinasDetailView.as_view(), name='Detalle de Rutinas'),
    path('rutinas/add', RutinasCreateView.as_view(), name='Formulario de Rutinas'),
    path('rutinas/update/<pk>', RutinasUpdateView.as_view(), name='Actualizar Rutinas'),
    path('rutinas/delete/<pk>', RutinasDeleteView.as_view(), name='Borrar Rutinas'),
    path('rutinas/buscar', rutinas_busqueda, name='Busqueda de Rutinas'),
    path('buscar_rutina', buscar_rutina, name='Buscar Rutinas')
]
from django.urls import path
from app_atletas.views import atletaCreateView, atletaDetailView, atletaDeleteView, atletaListView, atletaUpdateView, buscar, inicio, atleta_busqueda

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('buscar', buscar, name='Buscar'),
    path('atletas', atletaListView.as_view(), name='Atletas'),
    path('atletas/detalle/<pk>', atletaDetailView.as_view(), name='Detalle Atletas'),
    path('atletas/add', atletaCreateView.as_view(), name='Formulario de Atletas'),
    path('atletas/update/<pk>', atletaUpdateView.as_view(), name='Actualizar Atletas'),
    path('atletas/delete/<pk>', atletaDeleteView.as_view(), name='Borrar Atletas'),
    path('atletas/buscar', atleta_busqueda, name='Busqueda de Atletas'),
    ]

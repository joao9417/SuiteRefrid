from django.urls import path
from . import views

app_name = 'carga_termica'

urlpatterns = [
    path('calculo/', views.calculo_carga_termica, name='calculo_carga_termica'),
    path('calculo/<str:nombre_cuarto>/', views.calculo_carga_termica, name='calculo_carga_termica_nombre'),
]

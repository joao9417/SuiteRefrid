from django.urls import path
from . import views

app_name = 'carga_termica'

urlpatterns = [
    path('calculo/', views.calculo_carga_termica, name='calculo_carga_termica'),
    path('calculo/<str:nombre_cuarto>/', views.calculo_carga_termica, name='calculo_carga_termica_nombre'),
    path('api/evaporador-data/', views.obtener_datos_evaporador, name='obtener_datos_evaporador'),
    path('api/productos-data/', views.obtener_datos_producto, name='obtener_datos_producto'),
    path('api/lampara-data/', views.obtener_datos_lampara_led, name='obtener_datos_lampara'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='dashboard_inicio'),
    path('inicio/', views.inicio, name='dashboard_inicio'),
    path('crear/', views.crear_presupuesto, name='dashboard_crear_presupuesto'),
]

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    return render(request, "dashboard_principal/inicio.html", {})

@login_required
def crear_presupuesto(request):
    return render(request, "dashboard_principal/crear_presupuesto.html")

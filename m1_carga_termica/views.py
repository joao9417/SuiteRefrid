from django.shortcuts import render
from django.http import JsonResponse
from .models import Evaporador

#vista para renderizar la plantilla y manejar el formulario
def calculo_carga_termica(request, nombre_cuarto=None):
    """
    vista para el calculo de carga termica
    """
    #Si no se proporciona nombre de cuarto, usar uno por defecto
    if nombre_cuarto is None:
        nombre_cuarto = "Cuarto_Principal"

    #obtener todos los modelos de evaporadores de la base de datos secundaria.
    try:
        evaporadores_lista = Evaporador.objects.using('m1_carga_termica').values('modelo').order_by('modelo')
    except Exception as e:
        #manejar la excepcion si hay problemas de conexion con la BD
        print(F"error al obtener evaporadores: {e}")
        evaporadores_lista = []

    context = {
        'nombreCuarto': nombre_cuarto,
        'evaporadores_lista': evaporadores_lista,
    }

    if request.method == 'POST':
        #aqui procesamos los datos del formulario cuando los tengamos
        #por ahora solo mostramos el template
        return render(request, 'carga_termica/calculo_carga_termica.html', context)
    
    #metodo GET - mostrar el formulario vacio
    return render(request, 'carga_termica/calculo_carga_termica.html', context)


#vista para obtener los datos de un evaporador por su modelo
def obtener_datos_evaporador(request):
    modelo = request.GET.get('modelo')
    if not modelo:
        return JsonResponse({'error': 'Modelo no proporcionado'}, status=400)
    
    try:
        evap = Evaporador.objects.using('m1_carga_termica').get(modelo=modelo)
        #Mapear los datos del objeto modelo a un diccionario para la respuesta JSON
        data = {
            #nombres de las claves en el JSON: Nombres de las columnas de la BD
            'n_mot': evap.n_ventiladores,
            'm3_h_c_u': evap.volumen_aire_m3_h,
            'hp': evap.motor_axial_220v_60hz_a,
            'largo_mm': evap.largo_mm,
            'peso_kg': evap.pesos_kg,
        }
        return JsonResponse(data)
    except Evaporador.DoesNotExist:
        return JsonResponse({'error': 'Evaporador no encontrado'}, status=404)

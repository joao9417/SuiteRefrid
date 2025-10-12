from django.shortcuts import render
from django.http import JsonResponse
from .models import Evaporador
from .models import Productos

#vista para renderizar la plantilla y manejar el formulario
def calculo_carga_termica(request, nombre_cuarto=None):
    """
    vista para el calculo de carga termica
    """
    #Si no se proporciona nombre de cuarto, usar uno por defecto
    if nombre_cuarto is None:
        nombre_cuarto = "Cuarto_Principal"

    #1. OBTENER EVAPORADORES, para el dropdown
    try:
        evaporadores_lista = Evaporador.objects.using('m1_carga_termica').values('modelo').order_by('modelo')
    except Exception as e:
        #manejar la excepcion si hay problemas de conexion con la BD
        print(F"error al obtener evaporadores: {e}")
        evaporadores_lista = []

    #2. OBTENER PRODUCTOS, para el dropdown
    try:
        productos_lista = Productos.objects.using('m1_carga_termica').values('productos').order_by('productos')
        
    except Exception as e:
        #manejar la excepcion si hay problemas de conexion con la BD
        print(F"error al obtener productos: {e}")
        productos_lista = []
    
    context = {
        'nombreCuarto': nombre_cuarto,
        'evaporadores_lista': evaporadores_lista,
        'productos_lista': productos_lista,
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
    
 # Recupera los detalles de un producto especifico de la bd secuandaria y los devuelve en formato JSON    
def obtener_datos_producto(request):
    productos = request.GET.get('productos')
    if not productos:
        return JsonResponse({'error': 'Producto no proporcionado'}, status=400)
    try:
        prod = Productos.objects.using('m1_carga_termica').get(productos=productos)
        #Mapeo de los datos del objeto producto a un diccionario para la respuesta JSON
        data = {
            'punto_fusion': prod.punto_fusion_f,
            'cp_sobre': prod.cp_sobre_punto_cong_btu_lb_f,
            'cp_debajo': prod.cp_debajo_punto_cong_btu_lb_f,
            'latente_btu': prod.latente_btu_lb,
            'temp_0': prod.temp_0,
            'temp_5': prod.temp_5,
            'temp_10': prod.temp_10,
            'temp_15': prod.temp_15,
            'temp_20': prod.temp_20,
        }
        return JsonResponse(data)
    except Productos.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)

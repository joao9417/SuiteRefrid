from django.shortcuts import render

def calculo_carga_termica(request, nombre_cuarto=None):
    """
    vista para el calculo de carga termica
    """
    #Si no se proporciona nombre de cuarto, usar uno por defecto
    if nombre_cuarto is None:
        nombre_cuarto = "Cuarto_Principal"
    
    context = {
        'nombreCuarto': nombre_cuarto,
    }

    if request.method == 'POST':
        #aqui procesamos los datos del formulario cuando los tengamos
        #por ahora solo mostramos el template
        return render(request, 'carga_termica/calculo_carga_termica.html', context)
    
    #metodo GET - mostrar el formulario vacio
    return render(request, 'carga_termica/calculo_carga_termica.html', context)
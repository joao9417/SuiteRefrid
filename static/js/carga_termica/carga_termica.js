document.addEventListener('DOMContentLoaded', function() {

    // --Aplicación - % de congelación logica de mostrar/ocultar--
    const aplicacionSelect = document.getElementById('aplicacion');
    const porcentajeContainer = document.getElementById('porcentajeCongelacionContainer');

    function togglePorcentajeCongelacion() {
        if (aplicacionSelect.value === 'Cong Parcial') {
            porcentajeContainer.style.display = 'block';
        } else {
            porcentajeContainer.style.display = 'none';
        }
    }

    togglePorcentajeCongelacion();
    aplicacionSelect.addEventListener('change', togglePorcentajeCongelacion);
    
    
    // --Producto 2 logica de mostrar/ocultar--
    const toggleProducto2 = document.getElementById('toggleProducto2');
    const producto2 = document.getElementById('producto2');
    producto2.style.display = toggleProducto2.checked ? 'block' : 'none';
    toggleProducto2.addEventListener('change', function() {
        producto2.style.display = this.checked ? 'block' : 'none';
    });

    // --Producto 1 - Calor Evolución logica de mostrar/ocultar--
    const toggleCE = document.getElementById('toggleCalorEvolucion');
    const calorEvolucionBox = document.getElementById('calorEvolucionBox');
    calorEvolucionBox.style.display = toggleCE.checked ? 'block' : 'none';
    toggleCE.addEventListener('change', function() {
        calorEvolucionBox.style.display = this.checked ? 'block' : 'none';
    });

    // --Producto 2 - Calor Evolución logica de mostrar/ocultar--
    const toggleCE2 = document.getElementById('toggleCalorEvolucion2');
    const calorEvolucionBox2 = document.getElementById('calorEvolucionBox2');
    calorEvolucionBox2.style.display = toggleCE2.checked ? 'block' : 'none';
    toggleCE2.addEventListener('change', function() {
        calorEvolucionBox2.style.display = this.checked ? 'block' : 'none';
    });

    // --- Lógica del Menú Desplegable Modelo Evaporadores(Dropdown) ---
    
    const selectEvap = document.getElementById('evap');

    selectEvap.addEventListener('change', async function() {
        const modeloSeleccionado = this.value;
        if (modeloSeleccionado) {
            obtenerDatosEvaporador(modeloSeleccionado);
        } else {
            limpiarCamposEvaporador();
        }
    });
    
    // Función para limpiar todos los campos del evaporador
    function limpiarCamposEvaporador() {
        document.querySelector('input[name="n_mot"]').value = '';
        document.querySelector('input[name="m3_h_c_u"]').value = '';
        document.querySelector('input[name="hp"]').value = '';
        document.querySelector('input[name="watts"]').value = '';
        document.querySelector('input[name="largo_mm"]').value = '';
        updateCalculations();
    }

    // --funcion para calcular los cambios por hora del evaporador--
    function updateCalculations() {
        // 1. obtener valores de dimensiones del cuarto
        const largo = parseFloat(document.querySelector('input[name="l_m"]').value) || 0;
        const ancho = parseFloat(document.querySelector('input[name="a_m"]').value) || 0;
        const alto = parseFloat(document.querySelector('input[name="h_m"]').value) || 0;

        // 2. obtener caudal unitario del evaporador
        const caudal_unitario_raw = document.querySelector('input[name="m3_h_c_u"]').value;
        
        // normalizar el valor eliminando comas y puntos
        let caudal_unitario_clean = caudal_unitario_raw.replace(/\./g, '');

        // Convertir el valor limpio a número
        const caudal_unitario = parseFloat(caudal_unitario_clean) || 0; 
        
        // 3. obtener cantidad de evaporadores
        const cantidad_evap = parseFloat(document.querySelector('input[name="cant_evap"]').value) || 0; 

        // referencia al input de cambio por hora
        const inputCambioHora = document.querySelector('input[name="c_h"]');

        // 4. calcular cambios por hora
        // Volumen del cuarto = largo * ancho * alto (m3)
        // Caudal total = caudal unitario * cantidad de evaporadores (m3/h)
        // Cambios por hora = Caudal total / Volumen del cuarto (1/h)
        const volumen_cuarto = largo * ancho * alto; 
        const caudal_total = caudal_unitario * cantidad_evap; 

        let cambio_por_hora = 0;

        if (volumen_cuarto > 0) {
            cambio_por_hora = caudal_total / volumen_cuarto; 
        }
        
        // 5. mostrar el resultado en el input correspondiente, redondeado a 2 decimales
        inputCambioHora.value = cambio_por_hora.toFixed(2);
    }


    // --función para obtener datos del evaporador desde la API mediante AJAX--
    async function obtenerDatosEvaporador(modelo) { 
        try {
            const response = await fetch(`/carga-termica/api/evaporador-data/?modelo=${modelo}`);
            const data = await response.json();
            
            // Llenar los campos con los datos obtenidos
            document.querySelector('input[name="n_mot"]').value = data.n_mot || ''; 
            document.querySelector('input[name="m3_h_c_u"]').value = data.m3_h_c_u || '';
            document.querySelector('input[name="hp"]').value = data.hp || ''; 
            document.querySelector('input[name="largo_mm"]').value = data.largo_mm || '';

            updateCalculations(); 
        } catch (error) {
            console.error("Error al obtener datos del evaporador:", error);
            limpiarCamposEvaporador();
        }
    }

    // Escucha los cambios en los campos de dimensiones y cantidad de evaporadores
    const inputLargo = document.querySelector('input[name="l_m"]');
    const inputAncho = document.querySelector('input[name="a_m"]');
    const inputAlto = document.querySelector('input[name="h_m"]');
    const inputCantidadEvap = document.querySelector('input[name="cant_evap"]');

    //asignar eventos de escucha para los calculos en tiempo real 
    if (inputLargo) {
        inputLargo.addEventListener('input', updateCalculations);
    }

    if (inputAncho) {
        inputAncho.addEventListener('input', updateCalculations);
    }

    if (inputAlto) {
        inputAlto.addEventListener('input', updateCalculations);
    }

    if (inputCantidadEvap) {
        inputCantidadEvap.addEventListener('input', updateCalculations);
    }

    // inicializar los cálculos al cargar la página
    updateCalculations();



  // --logica de carros y rotacion producto 1 y 2 calculo--
function calcularRotacion(num) {
    
    const carrosInput = document.getElementById(`p${num}_carros`); 
    const rotacionInput = document.getElementById(`p${num}_rotacion`);

    if (carrosInput && rotacionInput) {
        const carrosValue = carrosInput.value;
        let carrosValueClean = carrosValue.replace(',', '.');
        const carrosNum = parseFloat(carrosValueClean);

        if (!isNaN(carrosNum)) {
            const rotacionCalculada = carrosNum * 350;
            rotacionInput.value = rotacionCalculada.toFixed(1);
        } else {
            rotacionInput.value = '0.0';
        }
    }
}

const p1_carrosInput = document.getElementById('p1_carros');
if (p1_carrosInput) {
    p1_carrosInput.addEventListener('input', () => calcularRotacion(1));
    calcularRotacion(1);
}

const p2_carrosInput = document.getElementById('p2_carros');
if (p2_carrosInput) {
    p2_carrosInput.addEventListener('input', () => calcularRotacion(2));
    calcularRotacion(2);
}


     // --- Lógica del Menú Desplegable Productos 1 y 2 (Dropdown) ---
    const selectProducto1 = document.getElementById('producto1');

    selectProducto1.addEventListener('change', async function() {
        const productoSeleccionado = this.value;
        if (productoSeleccionado) {
            obtenerDatosProducto(productoSeleccionado, 1);
        } else {
            limpiarCamposProducto(1);
        }
            
        });
    

    const selectProducto2 = document.getElementById('producto2');
    
    selectProducto2.addEventListener('change', async function() {
        const productoSeleccionado = this.value;
        if (productoSeleccionado) {
            obtenerDatosProducto(productoSeleccionado, 2);
        } else {
            limpiarCamposProducto(2);
        }

        });

    
// Función genérica para limpiar campos de producto
function limpiarCamposProducto(num) {
    document.querySelector(`input[name="p${num}_t_cong"]`).value = '';
    document.querySelector(`input[name="p${num}_cp_s_p"]`).value = '';
    document.querySelector(`input[name="p${num}_cp_b_p"]`).value = '';
    document.querySelector(`input[name="p${num}_calor_latente"]`).value = '';
    document.querySelector(`input[name="p${num}_calor_evolucion"]`).value = '';
}

// Función para obtener los datos del producto mediante la API AJAX
async function obtenerDatosProducto(producto, num) {
    try {
        //1. peticion a la API
        const response = await fetch(`/carga-termica/api/productos-data/?productos=${producto}`);
        const data = await response.json();

        let tCongCelsius = '';


        //2. obtener el valor de farenheit (convertimos a string para usar toUpperCase)
        const valorFarenheitAPI = String(data.t_cong || "").trim().toUpperCase();

        let valorFinalCampo = '';

        //3. logica condicional para asignacion/calculo
        if (valorFarenheitAPI === 'N/A') {
            //caso 1: si es N/A (no aplica)
            valorFinalCampo = 'N/A';
        } else if (valorFarenheitAPI === 'FALTA') {
            //caso 2: si es FALTA 
            valorFinalCampo = 'FALTA';
        } else {
            //caso 3: si es un valor numérico, convertir a Celsius
            const puntoFusionF = parseFloat(valorFarenheitAPI);

            if (!isNaN(puntoFusionF)) {
                // Es un número válido
                valorFinalCampo = ((puntoFusionF - 32) * 5 / 9).toFixed(2); // Convertir a Celsius
            } else {
                // No es un número válido
                console.warn(`[producto ${num}] Valor de punto de congelación no es un número válido: ${valorFarenheitAPI}`);
                valorFinalCampo = '';
            }
        }

        //4. llenar campos correspondientes
        const inputTcong = document.querySelector(`input[name="p${num}_t_cong"]`);

        if (inputTcong) {
            inputTcong.value = valorFinalCampo;
        }      

    } catch (error) {
        console.error(`Error al obtener datos del producto ${num}:`, error);
        limpiarCamposProducto(num);
    }
}    

});
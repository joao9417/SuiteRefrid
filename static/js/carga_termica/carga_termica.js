 // Script para mostrar/ocultar elementos en carga térmica
document.addEventListener('DOMContentLoaded', function() {
    // Para mostrar/ocultar Producto 2
    const toggle = document.getElementById('toggleProducto2');
    const producto2 = document.getElementById('producto2');

    if (toggle && producto2) {
        toggle.addEventListener('change', function() {
            producto2.style.display = this.checked ? 'block' : 'none';
        });
    }

    // Para Producto 1 - Calor Evolución
    const toggleCE = document.getElementById('toggleCalorEvolucion');
    const calorEvolucionBox = document.getElementById('calorEvolucionBox');

    if (toggleCE && calorEvolucionBox) {
        toggleCE.addEventListener('change', function() {
            calorEvolucionBox.style.display = this.checked ? 'block' : 'none';
        });
    }

    // Para Producto 2 - Calor Evolución
    const toggleCE2 = document.getElementById('toggleCalorEvolucion2');
    const calorEvolucionBox2 = document.getElementById('calorEvolucionBox2');

    if (toggleCE2 && calorEvolucionBox2) {
        toggleCE2.addEventListener('change', function() {
            calorEvolucionBox2.style.display = this.checked ? 'block' : 'none';
        });
    }
});
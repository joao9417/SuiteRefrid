from django.db import models

class Evaporador(models.Model):
    """
    modelo para almacenar información sobre los evaporadores.
    """
    #clave primaria modelo del evaporador
    modelo = models.CharField(max_length=255, primary_key=True)

    #columnas numericas
    capacidad_nominal_bth = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    n_ventiladores = models.IntegerField(null=True, blank=True)
    volumen_aire_m3_h = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tiro_aire_m = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    largo_mm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ancho_mm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    alto_mm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pesos_kg = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vol_ft3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    motor_axial_220v_60hz_w = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    motor_axial_220v_60hz_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    resistencias_220v_60hz_w = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    resistencias_220v_60hz_a = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    #columnas de texto
    conexion_liquido_in = models.CharField(max_length=50, null=True, blank=True)
    conexion_succion_in = models.CharField(max_length=50, null=True, blank=True)
    conexion_dren_npt_in = models.CharField(max_length=50, null=True, blank=True)
    motor_axial_220v_60hz_diam = models.CharField(max_length=50, null=True, blank=True)
    motor_axial_220v_60hz_acomet = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = False 
        db_table = 'evaporadores'
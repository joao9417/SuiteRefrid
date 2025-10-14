from django.db import models

class Evaporador(models.Model):    
    
    modelo = models.CharField(max_length=255, primary_key=True)
    
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

    conexion_liquido_in = models.CharField(max_length=50, null=True, blank=True)
    conexion_succion_in = models.CharField(max_length=50, null=True, blank=True)
    conexion_dren_npt_in = models.CharField(max_length=50, null=True, blank=True)
    motor_axial_220v_60hz_diam = models.CharField(max_length=50, null=True, blank=True)
    motor_axial_220v_60hz_acomet = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = False 
        db_table = 'evaporadores'

    
class Productos(models.Model):
    
    id = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)

    products = models.CharField(max_length=255, null=True, blank=True)
    productos = models.CharField(max_length=255, null=True, blank=True)
    tipo_producto = models.CharField(max_length=255, null=True, blank=True)
    punto_fusion_f = models.CharField(max_length=255, null=True, blank=True)
    cp_sobre_punto_cong_btu_lb_f = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cp_debajo_punto_cong_btu_lb_f = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    latente_btu_lb = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    temp_0 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    temp_5 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    temp_10 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    temp_15 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    temp_20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        managed = False 
        db_table = 'productos'


class Lamparas_led(models.Model):

    ref = models.CharField(max_length=255, primary_key=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    w = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lumens = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    factor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        managed = False 
        db_table = 'lamparas_led'

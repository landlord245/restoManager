# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Camarero(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=200, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    fecha_alta_camarero = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    def get_camareros():
        return Camarero.objects.all()

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Camarero'
        verbose_name_plural = 'Camareros'

class Mesa(models.Model):
    OPCIONES = (
        ('0', 'Interior'),
        ('1', 'Exterior')
    )

    lugar = models.CharField(max_length=20, choices=OPCIONES)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'

class Plato(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    def get_by_name(self, name:str):
        return self.objects.filter(nombre=name)

    def get_all_plato():
        return Plato.objects.all()

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Plato'
        verbose_name_plural = 'Platos'

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre;

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Bebida(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField()
    contiene_alcohol = models.BooleanField(default=False);

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Bebida'
        verbose_name_plural = 'Bebidas'

# RELACIONES

class Camarero_Mesa(models.Model):
    camarero = models.ForeignKey(Camarero, on_delete=models.DO_NOTHING)
    mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Camarero_Mesa'
        verbose_name_plural = 'Camarero_Mesas'

class Servicio_Cocina(models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.DO_NOTHING)
    servido = models.BooleanField(default=False)
    camarero_mesa = models.ForeignKey(Camarero_Mesa, on_delete=models.DO_NOTHING)
    hora_dia = models.DateTimeField()

    def __str__(self):
        pass
 
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Servicio_Cocina'
        verbose_name_plural = 'Servicio_Cocinas'

class Servicio_Barra(models.Model):
    bebida = models.ForeignKey(Bebida, on_delete=models.DO_NOTHING)
    servido = models.BooleanField(default=False)
    camarero_mesa = models.ForeignKey(Camarero_Mesa, on_delete=models.DO_NOTHING)
    hora_dia = models.DateTimeField()

    def __str__(self):
        pass
 
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Servicio_Barra'
        verbose_name_plural = 'Servicio_Barras'

class Plato_Categoria(models.Model):
    numero_menu = models.IntegerField(unique=True)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True)
    habilitado = models.BooleanField(blank=True, null=True, default=True)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Plato_Categoria'
        verbose_name_plural = 'Plato_Categorias'

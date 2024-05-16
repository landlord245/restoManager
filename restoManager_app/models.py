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

class Ubicacion(models.Model):
    OPCIONES = (
        ('0', 'Interior'),
        ('1', 'Exterior')
    )
    lugar = models.CharField(max_length=30, choices=OPCIONES)

    def __str__(self):
        return self.lugar

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'

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
        return self.nombre
    
    def get_by_name(self, name:str):
        return self.objects.filter(nombre=name)

    def get_all_categorias(self):
        return self.objects.all()

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Bebida(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField()
    contiene_alcohol = models.BooleanField(default=False);
    estado = models.BooleanField(blank=True, null=True, default=True)

    def __str__(self):
        return f'Nombre Categoria: {self.nombre}, Descripcion: {self.descripcion}, Contiene Alcohol: {self.contiene_alcohol}, Estado: {self.estado}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Bebida'
        verbose_name_plural = 'Bebidas'

# RELACIONES

class Plato_Categoria(models.Model):
    numero_menu = models.IntegerField(unique=True)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True)
    habilitado = models.BooleanField(blank=True, null=True, default=True)

    def __str__(self):
        return f'Numero de menu: {self.numero_menu}, Plato: {self.plato}, Categoría: {self.categoria}, Habilitado: {self.habilitado}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Plato_Categoria'
        verbose_name_plural = 'Plato_Categorias'

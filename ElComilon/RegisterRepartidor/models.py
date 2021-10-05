from django.db import models
from django.db.models.fields import related


# Create your models here.

# class Cargo(models.Model):
#     idcargo = models.IntegerField(primary_key=True)
#     descripcion = models.CharField(max_length=20)

#     class Meta:
#         managed = False
#         db_table = 'cargo'

# class Representante(models.Model):
#     rutrepresentante = models.CharField(primary_key=True, max_length=12)
#     nombres = models.CharField(max_length=20)
#     apellidos = models.CharField(max_length=20)
#     telefono = models.IntegerField()
#     correo = models.CharField(max_length=30)

#     class Meta:
#         managed = False
#         db_table = 'representante'

# class TipoRestaurante(models.Model):
#     idtiporest = models.IntegerField(primary_key=True)
#     descripcion = models.CharField(max_length=30)

#     class Meta:
#         managed = False
#         db_table = 'tipo_restaurante'


# class Restaurante(models.Model):
#     rutrestaurante = models.CharField(primary_key=True, max_length=12)
#     nombrerestaurante = models.CharField(max_length=20)
#     direccionrestaurante = models.CharField(max_length=30)
#     rutrepresentante = models.ForeignKey(Representante, models.DO_NOTHING, db_column='rutrepresentante')
#     idtiporest = models.ForeignKey('TipoRestaurante', models.DO_NOTHING, db_column='idtiporest')

#     class Meta:
#         managed = False
#         db_table = 'restaurante'

# class Repartidor(models.Model):
#     rutrepartidor = models.CharField(primary_key=True, max_length=12)
#     nombres = models.CharField(max_length=20)
#     apellidos = models.CharField(max_length=20)
#     fechacontrato = models.DateField()
#     usuario = models.CharField(max_length=15)
#     contrasena = models.CharField(max_length=20)
#     rutrestaurante = models.ForeignKey('Restaurante', models.DO_NOTHING, db_column='rutrestaurante')

#     class Meta:
#         managed = False
#         db_table = 'repartidor'

# class Trabajador(models.Model):
#     ruttrabajador = models.CharField(primary_key=True, max_length=12)
#     nombres = models.CharField(max_length=20)
#     apellidos = models.CharField(max_length=20)
#     fechacontrato = models.DateField()
#     usuario = models.CharField(max_length=15)
#     contrasena = models.CharField(max_length=20)
#     rutrestaurante = models.ForeignKey(Restaurante, models.DO_NOTHING, db_column='rutrestaurante')
#     idcargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='idcargo')

#     class Meta:
#         managed = False
#         db_table = 'trabajador'

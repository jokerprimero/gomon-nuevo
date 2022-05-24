from django.db import models

# Create your models here.

#Creación de tablas Go_mon
class Habilidad(models.Model):
    id_habilidad = models.IntegerField(primary_key=True, verbose_name='Id de la habilidad')
    nombre = models.CharField(max_length=50, verbose_name='Nombre del cuidador')

    def _str_(self):
        return self.nombre

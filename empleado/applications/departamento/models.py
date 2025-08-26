from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50) # name: variable en Django - Nombre> visualización en Admin
    short_name = models.CharField('Nombre Corto', max_length=50) # shot_name: variable en Django - Nombre Corto> visualización en Admin
    anulate = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name 
    
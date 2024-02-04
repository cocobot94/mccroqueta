from collections.abc import Iterable
from django.db import models


# Create your models here.
class Link(models.Model):
    key = models.SlugField(unique=True)
    description = models.CharField(max_length=50)
    url = models.URLField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.description


"""    def save(self, *args, **kwargs):
        if not self.id:  # Si es un nuevo objeto
            self.numero_ediciones = 0
        # Permitir edición solo una vez
        if self.numero_ediciones < 1:
            self.numero_ediciones += 1
            super().save(*args, **kwargs)
        else:
            # Puedes lanzar una excepción, imprimir un mensaje, o manejar de otra manera
            print("No se permite editar más de una vez.")"""

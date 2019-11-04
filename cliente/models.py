from django.db import models

# Create your models here.
class Cliente(models.Model):
    """Model definition for Cliente."""
    nombre = models.CharField( max_length=254)
    nit = models.CharField( max_length=10, default= "C/F")
    direccion = models.CharField( max_length=50, default = "ciudad")

    # TODO: Define fields here

    class Meta:
        """Meta definition for Cliente."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        """Unicode representation of Cliente."""
        return self.nombre
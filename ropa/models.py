from django.db import models

# Create your models here.
class Categoria(models.Model):
    """Model definition for MODELNAME."""
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.nombre

class Diseno(models.Model):
    """Model definition for Diseno."""
    nombre = models.CharField(max_length=254)

    def __str__(self):
        """Unicode representation of Diseno."""
        return self.nombre
   
# Create your models here.
class Ropa(models.Model):
    """Model definition for Ropa."""
    SIZE_CHOICES = [
        ("S", "SMALL"),
        ("M", "MEDIUM"),
        ("L", "LARGE"),
    ]
    COLOR_CHOICES = [
        ("Red", "Red"),
        ("Blue", "Blue"),
        ("Yellow", "Yellow"),
    ]

    imagen = models.ImageField(upload_to = "opciones")
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    tamano = models.CharField(max_length=50, choices = SIZE_CHOICES)
    color = models.CharField(max_length=50, choices = COLOR_CHOICES)
    tipo = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    diseno = models.ManyToManyField(Diseno, through="Asignacion")

    def __str__(self):
        """Unicode representation of Ropa."""
        return self.nombre + " " + self.tamano

    def get_image_url(self):         
        return self.imagen.url

class Asignacion(models.Model):
    """Model definition for MODELNAME."""
    COLOR_CHOICES = [
        ("Red", "Red"),
        ("Blue", "Blue"), 
        ("Yellow", "Yellow"),
        ]
    POSITION_CHOICES = [
        ("DelSuperiorD", "DelSuperiorD"),
        ("DelSuperiorI", "DelSuperiorI"), 
        ("DelInferiorD", "DelInferiorD"),
        ("DelInferiorI", "DelInferiorI"),
        ("TrasSuperiorD", "TrasSuperiorD"),
        ("TrasSuperiorI", "TrasSuperiorI"), 
        ("TrasInferiorD", "TrasInferiorD"),
        ("TrasInferiorI", "TrasInferiorI"),
        ]
    ropa = models.ForeignKey(Ropa, on_delete=models.CASCADE)
    diseno = models.ForeignKey(Diseno, on_delete=models.CASCADE)
    cantidad = models.IntegerField()     
    color = models.CharField(max_length=50,choices=COLOR_CHOICES, blank = True, null = True)
    posicion = models.CharField(max_length=50,choices=POSITION_CHOICES, blank = True, null = True)



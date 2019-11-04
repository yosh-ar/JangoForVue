from django.db import models
from ropa.models import Ropa
from cliente.models import Cliente
from django.db.models.signals import pre_save, post_save, post_delete

class Factura(models.Model):
    """Model definition for Invoice."""

    # TODO: return customer name from order

    PAYMENT_CHOICES = [
        ("cs", "cash"),
        ("ca", "card"),
        ("cu", "cupon"),
    ]
    numero = models.CharField(max_length=12)
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    orden = models.OneToOneField("Orden", on_delete=models.CASCADE)
    pago = models.CharField(max_length=2, choices=PAYMENT_CHOICES)

    def __str__(self):
        return str(self.orden.id)
    
    def total(self):
        return self.orden.total

def Factura_post_save_receiver(sender, instance, *args, **kwargs):
    """Calls update_status def from Order Model"""
    instance.orden.update_status("pa")

post_save.connect(Factura_post_save_receiver, sender=Factura)


class Orden(models.Model):
    """Customer orders and state management."""

    # TODO: delivery_type: To eat here or carry out

    STATUS_CHOICES = [
        ("re", "recibido"),
        ("pa", "pagado"),
        ("en", "entregado"),
    ]
    fecha = models.DateTimeField(auto_now_add=True)
    ropa = models.ManyToManyField(Ropa, through="OrdenDetail")
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="re")
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def update_total(self):
        total = 0
        ropas = self.ordendetail_set.all()
        for ropa in ropas:
            total += ropa.subtotal
        self.total = total
        self.save()

    def update_status(self, choice):
        self.status = choice
        self.save()

    def __str__(self):
        return str(self.id)


class OrdenDetail(models.Model):
    """Order detail as quantity of each ropa and price."""

    orden = models.ForeignKey(Orden, on_delete=models.PROTECT)
    ropa = models.ForeignKey(Ropa, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def remove(self):
        return self.ropa.remove_from_order()

    def __str__(self):
        return self.ropa.nombre

def order_ropa_pre_save_receiver(sender, instance, *args, **kwargs):
    """Pre saves the price and subtotal of orders."""
    qty = instance.cantidad
    if qty >= 1:
        precio = instance.ropa.precio
        subtotal = qty * precio
        instance.precio = precio
        instance.subtotal = subtotal


pre_save.connect(order_ropa_pre_save_receiver, sender=OrdenDetail)

def order_ropa_post_save_receiver(sender, instance, *args, **kwargs):
    """Calls update_total def from Order Model"""
    instance.orden.update_total()

post_save.connect(order_ropa_post_save_receiver, sender=OrdenDetail)

post_delete.connect(order_ropa_post_save_receiver, sender=OrdenDetail)



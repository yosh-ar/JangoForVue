from django.contrib import admin
from .models import Factura, Orden, OrdenDetail

# Register your models here.
class OrdenDetailInline(admin.TabularInline):
    '''Tabular Inline View for Pregunta'''      
    
    model = OrdenDetail     
    extra = 1

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    '''Admin View for Orden'''

    list_display = ('id', 'fecha', 'status','total')
    inlines = [
        OrdenDetailInline,
    ]
@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    '''Admin View for Factura'''

    list_display = ('numero','fecha', 'cliente','orden','pago','total')
    ordering = ('numero','fecha',)
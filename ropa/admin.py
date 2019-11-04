from django.contrib import admin
from .models import Ropa, Categoria, Diseno, Asignacion

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Diseno)
admin.site.register(Asignacion)
# Register your models here.
class AsignacionInline(admin.TabularInline):
    '''Tabular Inline View for Pregunta'''      
    
    model = Asignacion     
    extra = 1
    
@admin.register(Ropa)
class RopaAdmin(admin.ModelAdmin):
    '''Admin View for Ropa'''

    list_display = ('nombre', 'color', 'tamano')
    
    inlines = [
        AsignacionInline,
    ]

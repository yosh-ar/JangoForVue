from rest_framework import serializers
from .models import Ropa, Categoria, Diseno, Asignacion

class RopaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ropa
        fields = '__all__'
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class DisenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diseno
        fields = '__all__'
        
class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignacion
        fields = '__all__'
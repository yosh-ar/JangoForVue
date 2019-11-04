from rest_framework import viewsets
from .models import Ropa, Categoria, Diseno, Asignacion
from .serializers import RopaSerializer, CategoriaSerializer, DisenoSerializer, AsignacionSerializer

class RopaViewSet(viewsets.ModelViewSet):
    queryset = Ropa.objects.all()
    serializer_class = RopaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class DisenoViewSet(viewsets.ModelViewSet):
    queryset = Diseno.objects.all()
    serializer_class = DisenoSerializer

class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer
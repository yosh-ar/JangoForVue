from rest_framework import routers
from cliente.viewsets  import ClienteViewSet
from ropa.viewsets  import RopaViewSet, CategoriaViewSet

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'ropa', RopaViewSet)
from rest_framework import viewsets
from mesas.models import Mesa
from mesas.serializer import MesaSerializer

class MesasViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
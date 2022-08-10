from rest_framework import viewsets
from reservas.models import Reserva
from reservas.serializer import ResevaSerializer

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ResevaSerializer

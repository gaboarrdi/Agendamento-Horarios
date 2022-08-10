from django.contrib import admin
from django.urls import path, include
from mesas.views import MesasViewSet
from pessoas.views import PessoasViewSet
from reservas.views import ReservasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mesas',MesasViewSet),
router.register(r'pessoas',PessoasViewSet),
router.register(r'reservas',ReservasViewSet),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

from django.contrib import admin
from reservas.models import Reserva

class Reservas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'dia', 'periodo','mesa')
    list_display_links = ('id', 'nome', 'dia', 'periodo','mesa')
    search_fields = ('nome',)

admin.site.register(Reserva, Reservas)

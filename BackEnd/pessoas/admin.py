from django.contrib import admin
from pessoas.models import Pessoa

class Pessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'dia', 'periodo')
    list_display_links = ('id', 'nome', 'dia', 'periodo')
    search_fields = ('nome',)

admin.site.register(Pessoa, Pessoas)

from django.contrib import admin
from mesas.models import Mesa

class Mesas(admin.ModelAdmin):
    list_display = ('id','numero')
    list_display_links = ('id','numero')
    search_fields = ('numero',)

admin.site.register(Mesa, Mesas)

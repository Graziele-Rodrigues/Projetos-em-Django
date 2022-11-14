from core.models import Evento
from django.contrib import admin

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo',)

admin.site.site_header = 'Administração Agenda'
admin.site.register(Evento, EventoAdmin)
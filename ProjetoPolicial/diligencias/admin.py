from diligencias.models import Diligencia
from django.contrib import admin

# Register your models here.

class DiligenciaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_realizacao', 'dinheiro_apreendido']
    search_fields = ['nome']
    list_filter = ['data_realizacao']


admin.site.register(Diligencia, DiligenciaAdmin)
admin.site.site_header = 'Administração Tratore'

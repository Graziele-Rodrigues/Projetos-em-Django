from core.models import Cursos
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

class CursoResource(resources.ModelResource):
    class Meta:
        model = Cursos 
        import_id_fields = ('id_curso',)
        fields = ('id_curso', 'nome_curso', 'data_cadastro', 'login_cadastro', 'data_alteracao', 'login_alteracao',)

class CursosAdmin(ImportExportModelAdmin):
    list_display = ['id_curso', 'nome_curso', 'data_cadastro', 'login_cadastro', 'data_alteracao', 'login_alteracao']
    search_fields = ['id_curso', 'nome_curso']
    list_filter = ['data_cadastro', 'login_cadastro']
    list_per_page = 50
    resource_class = CursoResource 

admin.site.register(Cursos, CursosAdmin)



#importar csv via ação administrativa
""" class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Exportar selecionados em CSV" 

class CursosAdmin(admin.ModelAdmin, ExportCsvMixin):
    actions = ["export_as_csv"] """
from dashboard.models import Estudantes
from django.contrib import admin

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'city']
    search_fields = ['firstname', 'lastname', 'city']
    list_filter = ['firstname']

admin.site.register(Estudantes, StudentAdmin)
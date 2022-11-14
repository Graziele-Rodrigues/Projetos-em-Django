from core.models import Article
from django.contrib import admin

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'autor', 'date']
    search_fields = ['title', 'autor']
    list_filter = ['date', 'autor']

admin.site.register(Article, ArticleAdmin)
from django.contrib import admin
from .models import Catalog

# Register your models here.

# admin.site.register(Pokemon)

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    fields = ('nombre', 'pais', 'edad')
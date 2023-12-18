from django.contrib import admin
from .models import Pokemon

# Register your models here.

# admin.site.register(Pokemon)

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    fields = ('nombre', 'numero', 'tipo')
    list_display = ('nombre', 'generacion', 'tipo')
    search_fields = ('nombre',)
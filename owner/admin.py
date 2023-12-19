from django.contrib import admin
from .models import Owner

# Register your models here.

# admin.site.register(Pokemon)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    fields = ('nombre', 'pais', 'edad')
    list_display = ('nombre', 'pais', 'edad')
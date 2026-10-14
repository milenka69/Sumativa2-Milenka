from django.contrib import admin
from veterinaria.models import Cliente, Atencion

@admin.register(Cliente)
class ClienteAdmin (admin.ModelAdmin):
    list_display = ('nombre','rut','email','numero_telefono')
    list_editable = ('rut','email','numero_telefono')
    search_fields = ('nombre',)

@admin.register(Atencion)
class AtencionAdmin (admin.ModelAdmin):
    list_display = ('fecha', 'nombre_mascota', 'tipo_animal', 'costo', 'dueño')
    list_editable = ('nombre_mascota', 'tipo_animal', 'costo', 'dueño')
    search_fields = ('tipo_animal', 'fecha', 'dueño')
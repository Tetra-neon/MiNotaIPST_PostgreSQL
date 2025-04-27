from django.contrib import admin
from .models import Asignatura, Nota

class NotaInline(admin.TabularInline):
    model = Nota
    extra = 1  

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre_asignatura', 'eximicion', 'cantidad_evaluaciones', 'usuario')
    search_fields = ('nombre_asignatura',)
    list_filter = ('eximicion',)
    inlines = [NotaInline]  

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('nombre_evaluacion', 'asignatura', 'porcentaje', 'nota_obtenida', 'created_at')
    search_fields = ('nombre_evaluacion',)
    list_filter = ('asignatura',)

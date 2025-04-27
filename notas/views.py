# PRUEBA DE VISTA PARA VER EL FUNCIONAMIENTO SIN API AUN
from django.shortcuts import render, get_object_or_404
from .models import Asignatura

def prediccion_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    predicciones = asignatura.predecir_notas_faltantes()

    context = {
        'asignatura': asignatura,
        'predicciones': predicciones,
    }
    return render(request, 'notas/prediccion.html', context)
#Estamos agregando un endpoint de predicción
#Carga la asignatura por ID/Calcula las notas mínimas cuando se le pide
#Ejecuta la predicción automática
#Muestra el resultado en un HTML sencillo temporal
#Este HTML es sólo una vista provisional (de prueba interna) 
#para que podamos ver y validar que la predicción funciona antes de integrar con React


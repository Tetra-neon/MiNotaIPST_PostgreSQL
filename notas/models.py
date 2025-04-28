from django.db import models
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class Asignatura(models.Model):
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='asignaturas', null=True, blank=True)
    nombre_asignatura = models.CharField(max_length=100)
    # Promedio necesario para eximirse (5.3 o 5.5)
    eximicion = models.FloatField(default=5.3)
    cantidad_evaluaciones = models.PositiveIntegerField(default=4)

    def __str__(self):
        return self.nombre_asignatura

    def calcular_nota_promedio_requerida(self):
        notas = self.notas.all()

        suma_peso_obtenido = sum(
            [nota.nota_obtenida * nota.porcentaje for nota in notas if nota.nota_obtenida is not None])
        suma_porcentaje = sum(
            [nota.porcentaje for nota in notas if nota.nota_obtenida is not None])

        if suma_porcentaje >= 100:
            return None

        nota_requerida = ((self.eximicion * 100) -
                          suma_peso_obtenido) / (100 - suma_porcentaje)

        return round(nota_requerida, 1)

    def predecir_notas_faltantes(self):
        notas = self.notas.all()

        suma_peso_obtenido = sum(
                [nota.nota_obtenida * nota.porcentaje for nota in notas if nota.nota_obtenida is not None])
        suma_porcentaje = sum(
                [nota.porcentaje for nota in notas if nota.nota_obtenida is not None])

        evaluaciones_ingresadas = len([nota for nota in notas if nota.nota_obtenida is not None])
        evaluaciones_faltantes = self.cantidad_evaluaciones - evaluaciones_ingresadas

        porcentaje_faltante = 100 - suma_porcentaje

        # Si ya no falta porcentaje o no faltan evaluaciones, no hay nada que predecir
        if evaluaciones_faltantes <= 0 or porcentaje_faltante <= 0:
            return []

        nota_promedio_requerida = ((self.eximicion * 100) - suma_peso_obtenido) / porcentaje_faltante

        # Ajustamos para cada evaluación faltante
        predicciones = []
        notas_faltantes = [
            nota for nota in notas if nota.nota_obtenida is None]

        for nota in notas_faltantes:
            peso_relativo = nota.porcentaje / porcentaje_faltante
            nota_estimacion = nota_promedio_requerida / peso_relativo
            # Limitar entre 1.0 y 7.0
            nota_estimacion = max(min(nota_estimacion, 7.0), 1.0)

            predicciones.append({
                'evaluacion': nota.nombre_evaluacion,
                'nota_minima_sugerida': round(nota_estimacion, 1), #un decimal para la nota
            })

        # Si aún faltan evaluaciones que no están creadas en el sistema (sin registros)
        for i in range(evaluaciones_faltantes - len(notas_faltantes)):
            predicciones.append({
                'evaluacion': f"Evaluación Pendiente {i + 1}",
                'nota_minima_sugerida': round(nota_promedio_requerida, 1),
            })

        return predicciones


class Nota(models.Model):
    asignatura = models.ForeignKey(
        Asignatura, related_name='notas', on_delete=models.CASCADE)
    nombre_evaluacion = models.CharField(max_length=100)
    porcentaje = models.FloatField()
    nota_obtenida = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_evaluacion} - {self.asignatura.nombre_asignatura}"

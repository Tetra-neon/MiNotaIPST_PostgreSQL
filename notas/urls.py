from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsignaturaViewSet, NotaViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Asignatura #para saber de qué modelo estamos hablando
from django.shortcuts import get_object_or_404 #Para buscar la asignatura por id

router = DefaultRouter()
router.register(r'asignaturas', AsignaturaViewSet, basename='asignatura')
router.register(r'notas', NotaViewSet, basename='nota')

@api_view(['GET'])
def prediccion_view(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    predicciones = asignatura.predecir_notas_faltantes()
    return Response(predicciones)

urlpatterns = [
    path('', include(router.urls)),
    path('asignaturas/<int:asignatura_id>/prediccion/', prediccion_view, name='prediccion'),
]

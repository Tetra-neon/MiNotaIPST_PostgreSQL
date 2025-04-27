from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Asignatura, Nota
from .serializers import AsignaturaSerializer, NotaSerializer

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

@api_view(['GET'])
def prediccion_view(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    predicciones = asignatura.predecir_notas_faltantes()
    return Response(predicciones)

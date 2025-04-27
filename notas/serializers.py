from rest_framework import serializers
from .models import Asignatura, Nota

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'

class AsignaturaSerializer(serializers.ModelSerializer):
    notas = NotaSerializer(many=True, read_only=True)

    class Meta:
        model = Asignatura
        fields = '__all__'

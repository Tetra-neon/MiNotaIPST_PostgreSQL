from django.urls import path
from .views import prediccion_asignatura

urlpatterns = [
    path('prediccion/<int:asignatura_id>/', prediccion_asignatura, name='prediccion_asignatura'),
]

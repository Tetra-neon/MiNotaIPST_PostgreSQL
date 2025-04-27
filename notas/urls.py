from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsignaturaViewSet, NotaViewSet, prediccion_view

router = DefaultRouter()
router.register(r'asignaturas', AsignaturaViewSet, basename='asignatura')
router.register(r'notas', NotaViewSet, basename='nota')

urlpatterns = [
    path('', include(router.urls)),
    path('asignaturas/<int:asignatura_id>/prediccion/', prediccion_view, name='prediccion'),
]

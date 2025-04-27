from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsignaturaViewSet, NotaViewSet

router = DefaultRouter()
router.register(r'asignaturas', AsignaturaViewSet, basename='asignatura')
router.register(r'notas', NotaViewSet, basename='nota')

urlpatterns = [
    path('', include(router.urls)),
]

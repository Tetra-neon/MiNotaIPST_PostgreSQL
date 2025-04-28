from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)

    # Puedes agregar más campos personalizados aquí si quieres en el futuro
    # ejemplo: fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

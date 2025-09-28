from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    modelo de usuario personalizado, este modelo hereda todos los campos
    del usuario por defecto de django (username, mail, password, etc.)
    Aca se pueden agregar campos personalizados si los necesitas en el futuro.
    """
    pass

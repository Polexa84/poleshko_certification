from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Дополнительные поля для модели пользователя, если нужно

    def __str__(self):
        return self.username
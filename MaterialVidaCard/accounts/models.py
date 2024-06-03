# accounts/models.py

from django.db import models


class AuthorizedEmail(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

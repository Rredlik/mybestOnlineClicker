import django.contrib.auth.models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            ""
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("Такой пользователь уже зарегестрирован."),
        },
    )

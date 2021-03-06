from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


class AppUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="%(app_label)s_%(class)s_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="%(app_label)s_%(class)s_user_set",
        related_query_name="user",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.username


class OneTimeCode(models.Model):
    email = models.EmailField(verbose_name='Email')
    code = models.IntegerField(verbose_name=_('One-time code'))
    datetime = models.DateTimeField(default=datetime.now(), verbose_name=_('DateTime'))

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BulletinsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bulletins'
    verbose_name = _('Bulletins')

    def ready(self):
        pass

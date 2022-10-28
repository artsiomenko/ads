from django.apps import AppConfig

from django.dispatch import Signal


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = 'Ads'


user_registered = Signal('instance')

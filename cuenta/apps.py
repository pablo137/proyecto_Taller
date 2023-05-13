from django.apps import AppConfig


class CuentaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cuenta'
    verbose_name = 'perfiles'

    def ready(self) -> None:
        import cuenta.signals
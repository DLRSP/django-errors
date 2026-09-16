"""Django App's config for django-errors app"""

from django.apps import AppConfig


class DjangoErrorsConfig(AppConfig):
    """django-errors apps config"""

    name = "django_errors"

    def ready(self) -> None:
        from django_errors import py314_compat

        py314_compat.apply()

"""Customer app"""

from django.apps import AppConfig


class CustomersConfig(AppConfig):
    """Default config settings"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "customers"

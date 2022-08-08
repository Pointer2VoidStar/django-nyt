from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangoNytConfig(AppConfig):
    name = "django_nyt"
    verbose_name = _("Django Nyt")
    default_auto_field = 'django.db.models.BigAutoField'

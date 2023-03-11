from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "more_luca.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import more_luca.users.signals  # noqa F401
        except ImportError:
            pass

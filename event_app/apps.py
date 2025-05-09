# event_app/apps.py

# django
from django.apps import AppConfig


####################
# EVENT APP CONFIG #
####################
class EventAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name               = 'event_app'
    verbose_name       = 'Event Section'

    def ready(self):
        import event_app.signals                           # make the signals ready on app load

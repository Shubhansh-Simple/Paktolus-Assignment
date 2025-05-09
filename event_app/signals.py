# event_app/signals.py

# django
from django.db.models.signals import post_save
from django.dispatch          import receiver

# local
from event_app.models import Event
from event_app.tasks  import log_to_file


####################
# ON EVENT CREATED #
####################
@receiver(post_save, sender=Event)
def on_event_created(sender, instance, created, **kwargs):
    '''On every new event creation, call the log_to_file celery task'''

    if created:
        log_to_file.delay(instance.id)                     # call the celery task

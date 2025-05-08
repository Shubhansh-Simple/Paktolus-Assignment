# event_app/models.py

# django
from django.db import models


###############
# Event Model #
###############
class Event(models.Model):
    '''Event model for storing events of the application'''

    # FIELDS
    event_type = models.CharField(max_length=20, help_text='Stores the type of event occured')
    source     = models.CharField(max_length=20, help_text='Stores the source through which event originated')
    timestamp  = models.DateTimeField(auto_now_add=True, help_text='Stores the time at which event occured')


    class Meta:
        verbose_name        = 'Event'
        verbose_name_plural = 'Events'


    def __str__(self):
        return f"{self.event_type} from {self.source} at {self.timestamp}"

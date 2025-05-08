# event_app/admin.py

# django
from django.contrib import admin

# local
from event_app.models import Event


#####################
# EVENT MODEL ADMIN #
#####################
class EventAdmin(admin.ModelAdmin):
    '''Modify Event model representation on admin site'''

    # To improve visibility in admin site
    readonly_fields = ('id',)
    list_display    = ('id', 'event_type', 'source', 'timestamp')


# Register your models here.
admin.site.register(Event, EventAdmin)

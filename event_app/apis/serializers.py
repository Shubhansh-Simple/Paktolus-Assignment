# event_app/apis/serializers.py

# rest_framework
from rest_framework import serializers

# local
from event_app.models import Event


####################
# EVENT SERIALIZER #
####################
class EventSerializer(serializers.ModelSerializer):
    '''
    Serializer for event's model

    Payload
        {
            "event_type" : "login",
            "source"     : "mobile"
        }
    '''

    class Meta:
        model  = Event
        fields = '__all__'

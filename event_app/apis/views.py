# event_app/apis/views.py

"""
Event-related API views:
    - EventListCreateAPIView
    - EventRetrieveAPIView
"""

# rest_framework
from rest_framework          import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

# local
from event_app.models           import Event
from event_app.apis.serializers import EventSerializer


##############################
# EVENT LIST CREATE API VIEW #
##############################
class EventListCreateAPIView(ListCreateAPIView):
    '''
    Show all the events and allow user to create them as well
    '''

    queryset         = Event.objects.all()
    serializer_class = EventSerializer


    ############## 
    # EVENT LIST #
    ############## 
    def list(self, request, *args, **kwargs):
        '''
        Return the list of all events

        Response
            200 OK:
            [
                {
                    "id"        : 1,
                    "event_type": "login",
                    "source"    : "mobile",
                    "timestamp" : "2025-05-08T14:49:50.329578+05:30"
                },
                {...}, {...}, {...}
            ]
        '''
        return super().list(request, *args, **kwargs)


    ################
    # EVENT CREATE #
    ################
    def create(self, request, *args, **kwargs):
        '''
        Create a new event

        Payload
            {
                "event_type" : "login",
                "source"     : "mobile"
            }

        Response
            200 OK:
            {
                "id"     : 1,
                "detail" : "Event 'login' created successfully "
            }

        Error
            400 Bad Request:
            {
                "event_type" : [
                    "This field is required",
                    "This field may not be blank",
                ],
                "source" : [
                    "This field may not be null",
                    "Ensure this field has no more than 20 characters."
                ]
            }
        '''
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            print('Data is valid - ',serializer.validated_data)
            event = serializer.save()

            # Response
            response = {
                "id"     : event.id,
                "detail" : f"Event '{event.event_type}' created successfully"
            }

            # Success Message
            return Response(response, status=status.HTTP_201_CREATED)

        # Bad request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


###########################
# EVENT RETRIEVE API VIEW #
###########################
class EventRetrieveAPIView(RetrieveAPIView):
    '''
    Allow user to retrieve any specific event using their event id
    '''

    queryset         = Event.objects.all()
    serializer_class = EventSerializer

    ##################
    # EVENT RETRIEVE #
    ##################
    def retrieve(self, request, *args, **kwargs):
        '''
        Retrieve a specific event

        Response
            200 OK:
            {
                "id"        : 1,
                "event_type": "login",
                "source"    : "mobile",
                "timestamp" : "2025-05-08T14:49:50.329578+05:30"
            }

        Error
            404 Not Found:
            {
                "detail" : "No Event matches the given query."
            }
        '''
        return super().retrieve(request, *args, **kwargs)

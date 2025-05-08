# event_app/apis/urls.py

# django
from django.urls import path

# local
from event_app.apis.views import EventListCreateAPIView, EventRetrieveAPIView


# Parent Url - '/events/'
urlpatterns = [
    path('',          EventListCreateAPIView.as_view(), name='event-list' ),
    path('<int:pk>/', EventRetrieveAPIView.as_view() ,  name='event-detail'),
]

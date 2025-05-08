# Core/urls.py

# django
from django.contrib import admin
from django.urls    import path, include

# local
from Core.views import CustomPageNotFound, CustomInternalServerError


urlpatterns = [
    # for administration site ( for developers )
    path('admin/', admin.site.urls),

    # for event app
    path('events/', include('event_app.apis.urls')),
]


# Custom Error Page Not Found / Server Error ( NOTE: DEBUG=False )
handler404 = CustomPageNotFound
handler500 = CustomInternalServerError

# Core/urls.py
URL configuration for Core project.

# django
from django.contrib import admin
from django.urls    import path, include

# local
from Core.views import CustomPageNotFound, CustomInternalServerError


urlpatterns = [
    path('admin/', admin.site.urls),
]


# Custom Error Page Not Found / Server Error ( NOTE: DEBUG=False )
handler404 = CustomPageNotFound
handler500 = CustomInternalServerError

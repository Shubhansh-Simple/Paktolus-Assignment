# Core/middlewares.py

# python
import logging

# django
from django.http import JsonResponse 

# Using the logger defined in django's settings LOGGING
logger = logging.getLogger('middlewares')


############################
# REQUEST AUDIT MIDDLEWARE #
############################
class RequestAuditMiddleware:


    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        '''Log the requests and validate the presence of custom headers'''

        # Logging the request path and method into "request.log" file
        logger.info(f'"{request.method} {request.path}"')

        # Check for custom header presence in requests
        if 'X-Request-ID' not in request.headers:
            return JsonResponse({"detail" : "X-Request-ID header is required"}, status=400)

        # Calls the next middlewares or views
        response = self.get_response(request)
        
        return response

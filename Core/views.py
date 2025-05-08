# Core/views.py

# rest framework
from rest_framework           import status
from rest_framework.response  import Response
from rest_framework.renderers import JSONRenderer


###############################
# CUSTOM PAGE NOT FOUND ERROR #
###############################
def CustomPageNotFound(request, exception):
    '''
    Overriding default 404 error message of server. Now server returns JSON 404 response not html
    Make sure debug=False, in order to make it work

    RESPONSE EXAMPLE
        {
            "detail" : "Resource not found"
        }
    '''

    # Error
    error    = {"detail" : "Resource not found"}
    response = Response(error, status=status.HTTP_400_BAD_REQUEST)

    response.accepted_renderer   = JSONRenderer()
    response.accepted_media_type = "application/json"
    response.renderer_context    = {}

    return response


################################
# CUSTOM INTERNAL SERVER ERROR #
################################
def CustomInternalServerError(request):
    '''
    Overriding default 500 error message of server. Now server returns JSON 500 response not html
    Make sure debug=False, in order to make it work

    RESPONSE EXAMPLE
        {
            "detail" : "Internal Server Error"
        }
    '''

    # Error
    error    = {"detail" : "Internal Server Error"}
    response = Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    response.accepted_renderer   = JSONRenderer()
    response.accepted_media_type = "application/json"
    response.renderer_context    = {}

    return response

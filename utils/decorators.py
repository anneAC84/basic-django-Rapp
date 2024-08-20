from receipes.models import Receipe
from rest_framework.exceptions import NotFound
from rest_framework.response import Response


# Decorator function that handles all handler method exceptions
def handle_exceptions(handler_func):
    def wrapper(*args, **kwargs):
       try:
           return handler_func(*args, **kwargs)
       except (Receipe.DoesNotExist, NotFound) as e:
           print(type(e))
           return Response({ 'message': str(e)}, 404)
       except Exception as e:
           print(e.__class__.__name__)
           print(e)
           return Response('An unknown error occured', 500)
    return wrapper
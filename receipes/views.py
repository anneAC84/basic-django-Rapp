from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Receipe
from .serializers.common import ReceipeSerializer
# Create your views here.

# Path for this view : /receipes
class ReceipeListCreateView(APIView):
    pass

    # Index Route
    def get(self, request):
        receipes = Receipe.objects.all()
        serialized_receipes = ReceipeSerializer(receipes, many=True)# if we make a request that will return multiple results, remember to use many=True
        print(serialized_receipes.data)
        return Response(serialized_receipes.data)

    # Create Route
    def post(self, request):
        try:
           receipe_to_create = ReceipeSerializer(data=request.data)
           if receipe_to_create.is_valid():
              receipe_to_create.save()
              return Response(receipe_to_create.data, 201)
           print('validated error:', receipe_to_create.errors)
           return Response(receipe_to_create.errors, 400)
        except Exception as e:
           print('Error:', e)
           return Response('An error occured', 500)
        
    # Path for this view: /receipes/<int:receipeId>/
class ReceipeRetrieveUpdateDestroyView(APIView):

    # Retrieve/Show
    #method: GET
    def get (self, request, pk):
        try:
           receipe = Receipe.objects.get(pk=pk)
           serialized_receipe = ReceipeSerializer(receipe) # convert to dictionary
           return Response(serialized_receipe.data)
        except Receipe.DoesNotExist as e:
           print(e)
           return Response({'message': 'Receipe not found.'},404)
        except Exception as e:
           print(e.__class__.__name__)
           return Response({ 'error':'An unknown error occured'},500)
       

    #Update
    #Method: PUT
    def put(self, request, pk):
         
        try:
           receipe_to_update = Receipe.objects.get(pk=pk)
           serialized_receipe = ReceipeSerializer(receipe_to_update, data=request.data, partial=True) # convert to dictionary
           if serialized_receipe.is_valid():
              serialized_receipe.save()
              return Response(serialized_receipe.data)
           return Response(serialized_receipe.errors, 400)
        except Receipe.DoesNotExist as e:
           print(e)
           return Response({'message': 'Receipe not found.'},404)
        except Exception as e:
           print(e.__class__.__name__)
           return Response({ 'error':'An unknown error occured'},500)

    #Destroy
    
    #Method: DELETE
    def delete(self, request, pk):
        try:
            receipe_to_delete = Receipe.objects.get(pk=pk)
            receipe_to_delete.delete()
            return Response(status=204)
        except Receipe.DoesNotExist as e:
           print(e)
           return Response({'message': 'Receipe not found.'},404)
        except Exception as e:
           print(e)
           return Response({ 'error':'An unknown error occured'},500)
       


        
         
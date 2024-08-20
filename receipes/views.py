from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Receipe
from .serializers.common import ReceipeSerializer
from utils.decorators import handle_exceptions




# Create your views here.

# Path for this view : /receipes
class ReceipeListCreateView(APIView):
    pass

    # Index Route
    @handle_exceptions
    def get(self, request):
        receipes = Receipe.objects.all()
        serialized_receipes = ReceipeSerializer(receipes, many=True)# if we make a request that will return multiple results, remember to use many=True
        print(serialized_receipes.data)
        return Response(serialized_receipes.data)

    # Create Route
    @handle_exceptions
    def post(self, request):
        
        receipe_to_create = ReceipeSerializer(data=request.data)
        if receipe_to_create.is_valid():
            receipe_to_create.save()
            return Response(receipe_to_create.data, 201)
        print('validated error:', receipe_to_create.errors)
        return Response(receipe_to_create.errors, 400)
        
    # Path for this view: /receipes/<int:receipeId>/
class ReceipeRetrieveUpdateDestroyView(APIView):

    # Retrieve/Show
    #method: GET
    @handle_exceptions
    def get (self, request, pk):
        receipe = Receipe.objects.get(pk=pk)
        serialized_receipe = ReceipeSerializer(receipe) # convert to dictionary
        return Response(serialized_receipe.data)
       
       

    #Update
    #Method: PUT
    @handle_exceptions
    def put(self, request, pk):
        receipe_to_update = Receipe.objects.get(pk=pk)
        serialized_receipe = ReceipeSerializer(receipe_to_update, data=request.data, partial=True) # convert to dictionary
        if serialized_receipe.is_valid():
            serialized_receipe.save()
            return Response(serialized_receipe.data)
        return Response(serialized_receipe.errors, 400)
       
    #Destroy
    
    #Method: DELETE
    @handle_exceptions
    def delete(self, request, pk):
        receipe_to_delete = Receipe.objects.get(pk=pk)
        receipe_to_delete.delete()
        return Response(status=204)
        
       


        
         
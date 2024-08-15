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
    #def post(self):
       # pass
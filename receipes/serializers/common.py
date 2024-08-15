from rest_framework.serializers import ModelSerializer
from ..models import Receipe

class ReceipeSerializer(ModelSerializer):
    class Meta:
        model = Receipe
        fields = '__all__' # want all lines to be serialized
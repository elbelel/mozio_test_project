from rest_framework import serializers
from .models import Polygon
from provider.serializer import ProviderSerializer


class PolygonSerializer(serializers.ModelSerializer):

    provider = ProviderSerializer(required=True)

    class Meta:
        model = Polygon
        fields = ('id', 'name', 'provider','price', 'longitude', 'latitude')




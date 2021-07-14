from django.shortcuts import render

# Create your views here.

from .models import Polygon
from rest_framework import generics
from rest_framework.response import Response
from .serializer import PolygonSerializer


# Register API


class PolygonAPI(generics.GenericAPIView):
    serializer_class = PolygonSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        new_polygon = Polygon.objects.create(
            name=data["name"],
            price=data["price"],
            provider=data["provider"],
            longitude=data["longitude"],
            latitude=data["latitude"],
        )

        new_polygon.save()

        serializer = PolygonSerializer(new_polygon)
        return Response({
            "status": 200,
            "data": serializer.data
        })

    def get(self, request, pk):
        data = Polygon.objects.filter(pk=pk).first()
        polygon = PolygonSerializer(data, many=True)
        return Response({
            "data": polygon.data
        })

    def delete(self, request, pk):
        data = Polygon.objects.get(pk=pk)
        data.delete()
        return Response({
            "message": "user is deleted"
        })

    def put(self, request, pk):
        provider = Polygon.objects.get(pk=pk)
        update_provider = PolygonSerializer(provider, data=request.data)
        if update_provider.is_valid():
            update_provider.save()
            return Response({
                "message": "Polygon updated success fully"
            })
        return Response({
            "status": 400,
            "error": update_provider.errors
        })


class GetPolygonByGeoloc(generics.GenericAPIView):
    serializer_class = PolygonSerializer

    def get(self, request, longitude, latitude):
        data = Polygon.objects.filter(longitude=longitude, latitude=latitude).all()
        polygon = PolygonSerializer(data, many=True)
        return Response({
            "data": polygon.data
        })

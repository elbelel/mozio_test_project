from django.shortcuts import render

# Create your views here.

from .models import Provider
from rest_framework import generics
from rest_framework.response import Response
from .serializer import ProviderSerializer


# Register API


class ProviderAPI(generics.GenericAPIView):
    serializer_class = ProviderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "provider": ProviderSerializer(user, context=self.get_serializer_context()).data,
        })

    def get(self, request,pk, format=None ):
        data = Provider.objects.filter(pk=pk).first()
        providers = ProviderSerializer(data)
        return Response({
            "data": providers.data
        })

    def delete(self, request, pk):
        data = Provider.objects.get(pk=pk)
        data.delete()
        return Response({
            "message": "user is deleted"
        })

    def put(self, request, pk):
        provider = Provider.objects.get(pk=pk)
        update_provider = ProviderSerializer(provider, data=request.data)
        if update_provider.is_valid():
            update_provider.save()
            return Response({
                "message": "Provider updated success fully"
            })
        return Response({
            "status": 400,
            "error": update_provider.errors
        })


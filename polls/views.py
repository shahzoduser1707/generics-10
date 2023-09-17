from django.shortcuts import render
from .serializers import StreetSerializers
from rest_framework.response import Response
from .models import StreetModel
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class GetStreet(generics.ListAPIView):
      queryset = StreetModel.objects.all()
      serializer_class = StreetSerializers
      permission_classes = (IsAuthenticated,)

class CreateStreet(generics.CreateAPIView):
      queryset = StreetModel.objects.all()
      serializer_class = StreetSerializers
    
class GetCreateStreet(generics.ListCreateAPIView):
      queryset = StreetModel.objects.all()
      serializer_class = StreetSerializers

class DetailUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
      queryset = StreetModel.objects.all()
      serializer_class = StreetSerializers
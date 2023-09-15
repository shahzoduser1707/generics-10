from rest_framework import serializers
from .models import StreetModel


class StreetSerializers(serializers.ModelSerializer):
    class Meta:
        model = StreetModel
        fields = ('__all__')
from heat_map.models import IpvFour, IpvSix
from rest_framework import serializers


class IpvFourSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpvFour
        fields = '__all__'


class IpvSixSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpvSix
        fields = '__all__'
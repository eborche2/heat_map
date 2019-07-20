from heat_map.models import Ipv
from rest_framework import serializers


class IpvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ipv
        fields = '__all__'



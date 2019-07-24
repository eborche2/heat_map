from rest_framework import serializers

from heat_map.models import Ipv


class IpvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ipv
        fields = '__all__'



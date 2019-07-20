from rest_framework.viewsets import ModelViewSet

from heat_map.models import Ipv
from heat_map.serializer import IpvSerializer

class IpvViewSet(ModelViewSet):
    serializer_class = IpvSerializer
    entity_name = 'ipvfour'

    def get_queryset(self):
        bounds = get_query_parameters(self.request)
        for each in bounds:
            if not each:
                return Ipv.objects.none()
        cluster = Ipv.objects.filter(
            longitude__gte=float(bounds[0]),
            longitude__lte=float(bounds[1]),
            latitude__gte=float(bounds[2]),
            latitude__lte=float(bounds[3])
        )
        return cluster


def get_query_parameters(request):
    lower_long = request.query_params.get('lower_long')
    upper_long = request.query_params.get('upper_long')
    lower_lat = request.query_params.get('lower_lat')
    upper_lat = request.query_params.get('upper_lat')
    return [lower_long, upper_long, lower_lat, upper_lat]
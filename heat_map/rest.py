from rest_framework.viewsets import ModelViewSet

from heat_map.models import IpvSix, IpvFour
from heat_map.serializer import IpvFourSerializer, IpvSixSerializer


class IpvSixViewSet(ModelViewSet):
    serializer_class = IpvSixSerializer
    entity_name = 'ipvsix'

    def get_queryset(self):
        bounds = get_query_parameters(self.request)
        for each in bounds:
            if not each:
                return IpvSix.objects.none()
        return IpvSix.objects.filter(
            longitude__gte=bounds[0],
            longitude__lte=bounds[1],
            latitude__gte=bounds[2],
            latitude__lte=bounds[3]
        )


class IpvFourViewSet(ModelViewSet):
    serializer_class = IpvFourSerializer
    entity_name = 'ipvfour'

    def get_queryset(self):
        bounds = get_query_parameters(self.request)
        for each in bounds:
            if not each:
                return IpvFour.objects.none()
        cluster = IpvFour.objects.filter(
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
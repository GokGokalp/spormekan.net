from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from api.models import Firm, FirmOption
from api.serializers import FirmSerializer, FirmOptionSerializer
from api.managers import FirmOptionManager


# Create your views here.
class FirmViewSet(viewsets.ModelViewSet):

    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

    @detail_route(methods=['get'])
    def preference(self, pk=None):
        pass


class FirmPreferenceViewSet(viewsets.ModelViewSet):

    queryset = FirmOption.objects.all()
    serializer_class = FirmOptionSerializer

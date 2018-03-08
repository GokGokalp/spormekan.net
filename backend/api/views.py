from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from api.models import Firm
from api.serializers import FirmSerializer
from api.managers import FirmOptionManager


# Create your views here.
class FirmViewSet(viewsets.ModelViewSet):

    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

    @detail_route(methods=['get'])
    def preference(self, request):
        print(request)
        firm_option = FirmOptionManager().get(1)
        return Response(firm_option)

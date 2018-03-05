from rest_framework import viewsets
from api.models import Firm
from api.serializers import FirmSerializer

# Create your views here.


class FirmViewSet(viewsets.ModelViewSet):

    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

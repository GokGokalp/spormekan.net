from rest_framework import viewsets
from backend.api.models import Firm
from backend.api.serializers import FirmSerializer

# Create your views here.


class FirmViewSet(viewsets.ModelViewSet):

    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

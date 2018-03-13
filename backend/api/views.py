from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import detail_route
from api.serializers import FirmSerializer, FirmOptionSerializer
from api.models import Firm, FirmOption
from rest_framework import status, viewsets
import logging


class FirmOptionsViewSet(viewsets.ModelViewSet):
    queryset = FirmOption.objects.all()
    serializer_class = FirmOptionSerializer
    http_method_names = ['get', 'put']


class FirmViewSet(viewsets.ModelViewSet):
    logger = logging.getLogger(__name__)
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

    def get(self, request, format=None):
        try:
            firms = Firm.objects.all()
            serializer = FirmSerializer(firms, many=True)
            return Response(serializer.data)
        except Exception as exp:
            self.logger.exception(exp)
            return Response('An error occurred during process', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            serializer = FirmSerializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as exp:
            self.logger.exception(exp)
            return Response('An error occurred during process', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @detail_route(methods=['get'])
    def preference(self, request, pk=None):
        try:
            firm_option = FirmOption.objects.get(id=pk)
            serializer = FirmOptionSerializer(firm_option)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response('Not found.', status=status.HTTP_404_NOT_FOUND)
        except Exception as exp:
            self.logger.exception(exp)
            return Response('An error occurred during process', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

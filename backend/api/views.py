from rest_framework.views import APIView
from rest_framework.response import Response
import logging
from api.serializers import FirmSerializer
from api.models import Firm
from rest_framework import status


class FirmList(APIView):
    logger = logging.getLogger(__name__)

    def get(self, request, format=None):
        try:
            firms = Firm.objects.all()
            serializer = FirmSerializer(firms, many=True)
            return Response(serializer.data)
        except Exception as exp:
            logging.exception(exp)
            return Response('An error occurred during process', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format=None):
        try:
            serializer = FirmSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as exp:
            logging.exception(exp)
            return Response('An error occurred during process', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

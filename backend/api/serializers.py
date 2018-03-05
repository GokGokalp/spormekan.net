from api.models import Firm
from rest_framework import serializers


class FirmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Firm
        fields = ('id', 'contact_first_name', 'contact_last_name', 'name', 'email',
                  'password', 'phone_number', 'city', 'address', 'logo', 'firm_type')

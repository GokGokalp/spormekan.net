from api.models import Firm, FirmOption
from rest_framework import serializers


class FirmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Firm
        fields = ('id', 'contact_first_name', 'contact_last_name', 'name', 'email',
                  'password', 'phone_number', 'city', 'address', 'logo', 'firm_type')


class FirmOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FirmOption
        fields = ('remaining_membership_reminder_day', 'theme', 'sms_credit',
                  'is_remaining_membership_email_reminder_active', 'is_remaining_membership_sms_reminder_active')

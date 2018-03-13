from api.models import Firm, FirmOption
from rest_framework import serializers
from datetime import datetime
from django.core.exceptions import ValidationError


class FirmOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmOption
        fields = '__all__'


class FirmSerializer(serializers.ModelSerializer):
    MIN_LENGTH_OF_PASSWORD = 5
    REMAINING_MEMBERSHIP_REMINDER_DAY = 5
    DEFAULT_THEME = 'Black'
    DEFAULT_SMS_CREDIT = 0

    class Meta:
        model = Firm
        fields = (
            'contact_first_name',
            'contact_last_name',
            'name',
            'email',
            'password',
            'firm_type',
            'phone_number',
            'city',
            'address',
            'logo',
        )
        read_only_fields = (
            'created_date',
            'last_modify_date'
        )
        required_fields = (
            'contact_first_name',
            'contact_last_name',
            'name',
            'email',
            'password',
            'firm_type'
        )

        extra_kwargs = {fields: {'allow_null': False, 'required': True} for fields in required_fields}

    def validate(self, data):
        firm = Firm.objects.filter(email=data['email'])

        if firm.count() > 0:
            raise ValidationError('The email already exist in the database.')

        if len(data['password']) < self.MIN_LENGTH_OF_PASSWORD:
            raise ValidationError('Password too short.')

        return data

    def create(self, validated_data):
        firm_option = FirmOption.objects.create(
            remaining_membership_reminder_day=self.REMAINING_MEMBERSHIP_REMINDER_DAY,
            theme=self.DEFAULT_THEME,
            sms_credit=self.DEFAULT_SMS_CREDIT
        )

        validated_data['firm_option'] = firm_option
        validated_data['created_date'] = datetime.utcnow()

        return super(FirmSerializer, self).create(validated_data)

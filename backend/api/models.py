from django.db import models
from datetime import datetime

# Create your models here.


class FirmOption(models.Model):
    class Meta:
        db_table = 'FirmOptions'

    remaining_membership_reminder_day = models.IntegerField(null=True)
    theme = models.TextField()
    sms_credit = models.IntegerField(default=0)
    is_remaining_membership_email_reminder_active = models.BooleanField(default=False)
    is_remaining_membership_sms_reminder_active = models.BooleanField(default=False)


class Firm(models.Model):
    class Meta:
        db_table = 'Firms'

    id = models.AutoField(primary_key=True)
    contact_first_name = models.TextField()
    contact_last_name = models.TextField()
    name = models.TextField(max_length=100)
    email = models.EmailField()
    password = models.TextField(max_length=20)
    phone_number = models.TextField(max_length=20)
    city = models.TextField(max_length=50)
    address = models.TextField()
    logo = models.TextField()

    FIRM_TYPE_CHOICES = (
        ('FITNESS_CENTER', '0'),
        ('PERSONAL_TRAINER', '1'),
    )

    firm_type = models.CharField(max_length=1, choices=FIRM_TYPE_CHOICES, default=0)
    firm_option = models.OneToOneField(FirmOption, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now, blank=False)
    last_modify_date = models.DateTimeField(default=datetime.now, blank=True)
    is_deleted = models.BooleanField(default=False)

    objects = models.Manager()


class Member(models.Model):
    class Meta:
        db_table = 'Members'

    id = models.AutoField(primary_key=True)
    firm_id = models.IntegerField(null=False)
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=30)
    birth_date = models.DateTimeField(blank=True)

    GENDER = (
        ('MALE', '0'),
        ('FEMALE', '1')
    )

    gender = models.CharField(max_length=1, choices=GENDER, default='0')
    email = models.EmailField()
    phone_number = models.TextField(max_length=20)
    city = models.TextField(max_length=50)
    address = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=False)
    last_modify_date = models.DateTimeField(default=datetime.now, blank=True)
    is_deleted = models.BooleanField(default=False)


class Membership(models.Model):
    class Meta:
        db_table = 'Memberships'

    id = models.AutoField(primary_key=True)
    firm_id = models.IntegerField(null=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    begin_date = models.DateTimeField(default=datetime.now, blank=False)
    end_date = models.DateTimeField(default=datetime.now, blank=False)
    is_active = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    currency_code = models.CharField(max_length=3)


class BodyMeasurement(models.Model):
    class Meta:
        db_table = 'BodyMeasurements'

    id = models.AutoField(primary_key=True)
    firm_id = models.IntegerField(null=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    measurement_date = models.DateTimeField(default=datetime.now, blank=False)
    kg = models.FloatField()
    body_fat_percentage = models.FloatField()
    body_water_percentage = models.FloatField()
    body_muscle_percentage = models.FloatField()
    right_bicep_size_in_cm = models.FloatField()
    left_bicep_size_in_cm = models.FloatField()
    chest_size_in_cm = models.FloatField()
    buttock_size_in_cm = models.FloatField()
    waist_size_in_cm = models.FloatField()
    created_date = models.DateTimeField(default=datetime.now, blank=False)
    last_modify_date = models.DateTimeField(default=datetime.now, blank=True)
    is_deleted = models.BooleanField(default=False)


class NotificationHistories(models.Model):
    class Meta:
        db_table = 'NotificationHistories'

    id = models.AutoField(primary_key=True)
    firm_id = models.IntegerField(null=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    NOTIFICATION_TYPE = (
        ('REMAINING_MEMBERSHIP_REMINDER', 0)
    )

    notification_type = models.CharField(max_length=1, choices=NOTIFICATION_TYPE, default='0')
    is_sms_sent = models.BooleanField(default=False)
    is_email_sent = models.BooleanField(default=False)
    notification_date = models.DateTimeField(default=datetime.now, blank=False)
    created_date = models.DateTimeField(default=datetime.now, blank=False)
    last_modify_date = models.DateTimeField(default=datetime.now, blank=True)
    is_deleted = models.BooleanField(default=False)


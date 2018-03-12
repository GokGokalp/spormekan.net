from django.db import models
from datetime import datetime


class FirmOption(models.Model):

    # Attributes
    id = models.AutoField(primary_key=True)
    remaining_membership_reminder_day = models.IntegerField(null=True)
    theme = models.TextField(null=True, blank=True)
    sms_credit = models.IntegerField(default=0)
    is_remaining_membership_email_reminder_active = models.BooleanField(default=False)
    is_remaining_membership_sms_reminder_active = models.BooleanField(default=False)

    # Managers
    objects = models.Manager()

    # Meta
    class Meta:
        db_table = 'FirmOptions'


class Firm(models.Model):

    # Attributes
    id = models.AutoField(primary_key=True)
    contact_first_name = models.TextField()
    contact_last_name = models.TextField()
    name = models.TextField(max_length=100)
    email = models.EmailField()
    password = models.TextField(max_length=20)
    phone_number = models.TextField(max_length=20, blank=True, null=True)
    city = models.TextField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)

    FITNESS_CENTER, PERSONAL_TRAINER = range(2)
    FIRM_TYPE_CHOICES = (
        (FITNESS_CENTER, 'Fitness Center'),
        (PERSONAL_TRAINER, 'Personal Trainer'),
    )

    firm_type = models.CharField(max_length=1, choices=FIRM_TYPE_CHOICES, default=FITNESS_CENTER)
    firm_option = models.OneToOneField(FirmOption, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now, blank=False)
    last_modify_date = models.DateTimeField(default=datetime.now, blank=True)
    is_deleted = models.BooleanField(default=False)

    # Managers
    objects = models.Manager()

    # Meta
    class Meta:
        db_table = 'Firms'
        ordering = ['-id']


class Member(models.Model):
    # Attributes
    id = models.AutoField(primary_key=True)
    firm_id = models.IntegerField(null=False)
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=30)
    birth_date = models.DateTimeField(blank=True)
    UNKNOWN, MALE, FEMALE = range(3)
    GENDER = (
        (UNKNOWN, 0),
        (MALE, 1),
        (FEMALE, 2)
    )

    gender = models.CharField(max_length=1, choices=GENDER, default=UNKNOWN)
    email = models.EmailField()
    phone_number = models.TextField(max_length=20, blank=True)
    city = models.TextField(max_length=50)
    address = models.TextField(blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=False)
    last_modify_date = models.DateTimeField(default=datetime.now, blank=True)
    is_deleted = models.BooleanField(default=False)

    # Meta
    class Meta:
        db_table = 'Members'
        ordering = ['-id']


class Membership(models.Model):
    # Attributes
    id = models.AutoField(primary_key=True)
    firm_id = models.IntegerField(null=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    begin_date = models.DateTimeField(default=datetime.now, blank=False)
    end_date = models.DateTimeField(default=datetime.now, blank=False)
    is_active = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    currency_code = models.CharField(max_length=3)

    # Meta
    class Meta:
        db_table = 'Memberships'
        ordering = ['-id']


class BodyMeasurement(models.Model):
    # Attributes
    id = models.AutoField(primary_key=True)
    firm_id = models.IntegerField(null=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    measurement_date = models.DateTimeField(default=datetime.now)
    kg = models.FloatField(blank=True)
    body_fat_percentage = models.FloatField(blank=True)
    body_water_percentage = models.FloatField(blank=True)
    body_muscle_percentage = models.FloatField(blank=True)
    right_bicep_size_in_cm = models.FloatField(blank=True)
    left_bicep_size_in_cm = models.FloatField(blank=True)
    chest_size_in_cm = models.FloatField(blank=True)
    buttock_size_in_cm = models.FloatField(blank=True)
    waist_size_in_cm = models.FloatField(blank=True)
    created_date = models.DateTimeField(default=datetime.now)
    last_modify_date = models.DateTimeField(default=datetime.now)
    is_deleted = models.BooleanField(default=False)

    # Meta
    class Meta:
        db_table = 'BodyMeasurements'
        ordering = ['-id']


class NotificationHistories(models.Model):
    # Attributes
    id = models.AutoField(primary_key=True)
    firm_id = models.IntegerField(null=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    REMAINING_MEMBERSHIP_REMINDER, CAMPAIGN = range(2)
    NOTIFICATION_TYPE = (
        (REMAINING_MEMBERSHIP_REMINDER, 'Remaining Membership Reminder'),
        (CAMPAIGN, 'Campaign')
    )

    notification_type = models.CharField(max_length=1, choices=NOTIFICATION_TYPE, default=REMAINING_MEMBERSHIP_REMINDER)
    is_sms_sent = models.BooleanField(default=False)
    is_email_sent = models.BooleanField(default=False)
    notification_date = models.DateTimeField(default=datetime.now, blank=False)
    created_date = models.DateTimeField(default=datetime.now, blank=False)
    last_modify_date = models.DateTimeField(default=datetime.now, blank=True)
    is_deleted = models.BooleanField(default=False)

    # Meta
    class Meta:
        db_table = 'NotificationHistories'

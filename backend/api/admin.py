from django.contrib import admin
from api.models import FirmOption, Firm, Member, Membership, BodyMeasurement, NotificationHistories


# Register your models here.

admin.site.register(FirmOption)
admin.site.register(Firm)
admin.site.register(Member)
admin.site.register(Membership)
admin.site.register(BodyMeasurement)
admin.site.register(NotificationHistories)

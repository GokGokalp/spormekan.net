from django.db import models


class FirmOptionManager(models.Manager):
    def create(self, remaining_membership_reminder_day, theme,
               sms_credit, is_remaining_membership_email_reminder_active,
               is_remaining_membership_sms_reminder_active):

        return super(FirmOptionManager, self).create(
            remaining_membership_reminder_day=remaining_membership_reminder_day, theme=theme,
            sms_credit=sms_credit,
            is_remaining_membership_email_reminder_active=is_remaining_membership_email_reminder_active,
            is_remaining_membership_sms_reminder_active=is_remaining_membership_sms_reminder_active)

    def get(self, pk):
        firm_option = super(FirmOptionManager, self).filter(Id=pk)
        return firm_option


class FirmManager(models.Manager):
    def create(self, contact_first_name, contact_last_name, name,
               email, password, phone_number, city, address, logo, firm_type):
        try:
            firm_option = FirmOptionManager().create(0, 'black', 0)

            if firm_option.id is None:
                return None

            return super(FirmManager, self).create(contact_first_name=contact_first_name, contact_last_name=contact_last_name, name=name,
                                                   email=email, password=password, phone_number=phone_number, city=city,
                                                   address=address, logo=logo, firm_type=firm_type, firm_option=firm_option)

        except RuntimeError:
            pass

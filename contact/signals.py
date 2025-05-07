from django.db.models.signals import post_save
from django.dispatch import receiver
from .email_config import send_mail
from .models import Contact

@receiver(post_save, sender = Contact)
def send_contact_info(sender,instance,created,**kwargs):
    if created:
        send_mail(instance.email,instance.subject,instance.message)
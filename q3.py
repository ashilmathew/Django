from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    with transaction.atomic():
        print("Signal running within a transaction")
        # Your transaction logic here

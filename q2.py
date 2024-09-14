import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

# Saving an instance of MyModel
my_instance = MyModel.objects.create(field1="value")

# Output will be:
# Signal running in thread: MainThread (or whatever the thread is)

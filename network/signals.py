from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Network

@receiver(pre_save, sender=Network)
def update_level(sender, instance, **kwargs):
    if instance.supplier:
        instance.level = instance.supplier.level + 1
    else:
        instance.level = 0
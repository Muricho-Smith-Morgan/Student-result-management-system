from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Mark
from uuid import uuid4
@receiver(pre_save,sender = Result )
def generate_id(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid4())[:20]
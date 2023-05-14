from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Perfil

@receiver(post_save, sender=Perfil)
def add_user_to_consumidor_group(sender, instance, created, **kwargs):
    if created:
        try:
            consumidor = Group.objects.get(name='Consumidor')
        except Group.DoesNotExist:
            consumidor = Group.objects.create(name='Consumidor')
            consumidor = Group.objects.create(name='Emprendedor')
            consumidor = Group.objects.create(name='Administrativo')
        instance.user.groups.add(consumidor)
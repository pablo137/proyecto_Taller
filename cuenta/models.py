from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#Perfil de usuario:
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil', verbose_name='Usuario')
    img = models.ImageField(default='users/img_defecto_guzx7h.jpg', upload_to='users/', verbose_name='Imagen de perfil')
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name='Biografia')
    telf = models.CharField(max_length=50, blank=True, null=True, verbose_name='Telefono')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['id']
    
    def __str__(self):
        return "Perfil: {0}".format(self.user.username)
    
def crear_user_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

def save_user_perfil(sender, instance, **kwargs):
    instance.perfil.save()

post_save.connect(crear_user_perfil, sender=User)
post_save.connect(save_user_perfil, sender=User)
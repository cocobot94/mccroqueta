from django.db import models
from apps.users.models import User
from ckeditor.fields import RichTextField

from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    if kwargs.get("created"):
        Profile.objects.create(user=instance)

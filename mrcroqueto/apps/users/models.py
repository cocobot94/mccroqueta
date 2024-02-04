from django.db import models
from django.contrib.auth.models import AbstractUser

from django.dispatch import receiver
from django.db.models.signals import post_save

from django.db.models import F, Q


def custom_upload_to(instance, filename):
    try:
        old_instance = User.objects.get(pk=instance.pk)
        old_instance.image.delete()
        return "users/" + filename
    except User.DoesNotExist:
        return "users/" + filename


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )

    class Meta:
        ordering = ["username"]

from django.db import models


def custom_upload_to(instance, filename):
    try:
        old_instance = News.objects.get(pk=instance.pk)
        if old_instance.image:
            old_instance.image.delete()
        return "news/" + filename
    except News.DoesNotExist:
        return "news/" + filename


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"
        ordering = ["-created"]

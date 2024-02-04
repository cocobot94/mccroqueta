from django.db import models
from apps.users.models import User
from ckeditor.fields import RichTextField


def custom_upload_to(instance, filename):
    try:
        old_instance = Post.objects.get(pk=instance.pk)
        old_instance.image.delete()
        return "blog/" + filename
    except Post.DoesNotExist:
        return "blog/" + filename


# Create your models here.
class CategoryPost(models.Model):
    description = models.CharField(max_length=70, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    category_post = models.ForeignKey(CategoryPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=False)
    vistas = models.IntegerField(default=0)
    like = models.ManyToManyField(User, blank=True)
    dislike = models.ManyToManyField(User, blank=True, related_name="dislikes")
    fav = models.ManyToManyField(User, blank=True, related_name="favoritos")

    def __str__(self) -> str:
        return self.title

    def aumentar_vistas(self):
        self.vistas += 1
        self.save()

    class Meta:
        ordering = ["-created"]


class Comments(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments_post"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_user"
    )
    content = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

from rest_framework import serializers
from apps.blog.models import Post, Comments, CategoryPost


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "title": instance.title,
            "image": instance.image.url if instance.image else "",
            "created": instance.created,
            "state": instance.state,
            "vistas": instance.vistas,
            "author": instance.author.username,
            "category_product": instance.category_post.description
            if instance.category_post
            else "",
        }


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "content": instance.content,
            "created": instance.created,
            "post": instance.post.title,
            "user": instance.user.username,
        }


class CategoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPost
        fields = "__all__"

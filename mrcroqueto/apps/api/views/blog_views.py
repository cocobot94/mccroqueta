from rest_framework import viewsets
from apps.api.serializers.blog_serializer import (
    PostSerializer,
    CategoryPostSerializer,
    CommentsSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class CategoryPostViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryPostSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

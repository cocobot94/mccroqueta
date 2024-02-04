from rest_framework import viewsets
from apps.api.serializers.news_serializer import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

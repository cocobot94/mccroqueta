from rest_framework import viewsets
from apps.api.serializers.link_serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

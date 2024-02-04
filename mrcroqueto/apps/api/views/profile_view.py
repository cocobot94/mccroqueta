from apps.api.serializers.profile_serializer import ProfileSerializer
from rest_framework import viewsets


class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

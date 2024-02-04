from apps.registration.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "bio": instance.bio if instance.bio else "",
            "created": instance.created,
            "updated": instance.updated,
            "user": instance.user.username,
        }

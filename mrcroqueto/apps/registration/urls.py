from django.urls import path
from .views import SignUpView, ProfileView, ProfileUpdate, BioUpdate, ImageUpdate


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    path("profile_update/", ProfileUpdate.as_view(), name="profile_update"),
    path("image_update/", ImageUpdate.as_view(), name="image_update"),
    path("bio_update/", BioUpdate.as_view(), name="bio_update"),
]

from django.urls import path, include
from .views import UserListView, UserDeleteView, Followers, Following

urlpatterns = [
    path("", UserListView.as_view(), name="users"),
    path("delete_user/<int:pk>/", UserDeleteView.as_view(), name="delete_user"),
    path("followers/<int:pk>/", Followers.as_view(), name="followers"),
    path("following/<int:pk>/", Following.as_view(), name="following"),
]

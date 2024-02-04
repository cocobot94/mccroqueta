from django.urls import path
from apps.blog.views import (
    PostViewSet,
    PostDetailView,
    PostDeleteView,
    PostRevissionViewSet,
    PostCategoryViewSet,
    PostDetailRevissionView,
    PostUpdateView,
    PostCreateView,
    CommentsListView,
    CommentsCreate,
    PostsFavoritesViewSet,
)

urlpatterns = [
    path("", PostViewSet.as_view(), name="posts"),
    path("posts_favorites/", PostsFavoritesViewSet.as_view(), name="posts_favorites"),
    path("post_detail/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post_delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
    path(
        "post_category/<int:pk>/", PostCategoryViewSet.as_view(), name="post_category"
    ),
    path("post_revission/", PostRevissionViewSet.as_view(), name="post_revission"),
    path(
        "post_detail_revission/<int:pk>/",
        PostDetailRevissionView.as_view(),
        name="post_detail_revission",
    ),
    path("post_update/<int:pk>", PostUpdateView.as_view(), name="post_update"),
    path("post_create/", PostCreateView.as_view(), name="post_create"),
    path("comments/<int:pk>/", CommentsListView.as_view(), name="comments"),
    path("comment_create/<int:pk>/", CommentsCreate.as_view(), name="comment_create"),
]

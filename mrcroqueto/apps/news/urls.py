from django.urls import path, include
from apps.news.views import NewsListView, NewsDetailView

urlpatterns = [
    path("", NewsListView.as_view(), name="news"),
    path("news_detail/<int:pk>/", NewsDetailView.as_view(), name="news_detail"),
]

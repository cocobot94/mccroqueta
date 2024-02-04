from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from apps.news.models import News
from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.


@method_decorator(login_required, name="dispatch")
class NewsListView(ListView):
    model = News
    template_name = "news/news.html"
    context_object_name = "news"

    def get_queryset(self) -> QuerySet[Any]:
        news = self.model.objects.all()
        paginator = Paginator(news, 3)
        page = self.request.GET.get("page")
        news = paginator.get_page(page)
        return news

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        params = self.request.GET.get("search")
        news = self.model.objects.all()
        if params:
            news = news.filter(
                Q(title__icontains=params) | Q(content__icontains=params)
            ).distinct()
        else:
            paginator = Paginator(news, 3)
            page = self.request.GET.get("page")
            news = paginator.get_page(page)
        context[self.context_object_name] = news
        return context


@method_decorator(login_required, name="dispatch")
class NewsDetailView(DetailView):
    model = News
    template_name = "news/news_detail.html"

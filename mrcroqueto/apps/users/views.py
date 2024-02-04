from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

from .models import User

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
@method_decorator(login_required, name="dispatch")
class UserListView(ListView):
    model = User
    template_name = "users/users.html"
    context_object_name = "users"

    def get_queryset(self) -> QuerySet[Any]:
        users = self.model.objects.filter(is_active=True)
        return users

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        params = self.request.GET.get("search")
        users = self.model.objects.filter(is_active=True)

        if params:
            users = users.filter(
                Q(username__icontains=params)
                | Q(first_name__icontains=params)
                | Q(last_name__icontains=params)
            )
        else:
            paginator = Paginator(users, 6)
            page = self.request.GET.get("page")
            users = paginator.get_page(page)
        context[self.context_object_name] = users
        return context


@method_decorator(login_required, name="dispatch")
class UserDeleteView(DeleteView):
    model = User
    template_name = "users/delete_user.html"

    def get_success_url(self) -> str:
        return reverse_lazy("users") + "?delete"


@method_decorator(login_required, name="dispatch")
class Followers(DetailView):
    model = User
    template_name = "users/followers.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["followers"] = self.get_object().followers.all()

        return context


@method_decorator(login_required, name="dispatch")
class Following(DetailView):
    model = User
    template_name = "users/following.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        users = self.get_object().following.filter(is_active=True)

        paginator = Paginator(users, 10)
        page = self.request.GET.get("page")
        users = paginator.get_page(page)
        context["following"] = users
        return context

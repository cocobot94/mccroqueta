from typing import Any
from django.db.models.base import Model as Model
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from apps.registration.models import Profile
from apps.users.forms import UserForm
from apps.users.models import User
from django import forms
from .forms import UserFormPro, ProfileForm, UserFormImage
from django.urls import reverse_lazy
from django.shortcuts import redirect
from apps.blog.models import Post

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.


class SignUpView(CreateView):
    form_class = UserForm
    template_name = "registration/signup.html"

    def get_success_url(self) -> str:
        return reverse_lazy("login") + "?register"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["username"].widget = forms.TextInput(
            attrs={"class": "form-control mb-2"}
        )
        form.fields["email"].widget = forms.EmailInput(
            attrs={"class": "form-control mb-2"}
        )
        form.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": "form-control mb-2"}
        )
        form.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": "form-control mb-2"}
        )
        return form


@method_decorator(login_required, name="dispatch")
class ProfileView(DetailView):
    model = Profile
    template_name = "registration/profile.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        seguir = request.GET.get("seguir")
        noseguir = request.GET.get("noseguir")
        if seguir:
            self.follow()
        elif noseguir:
            self.unfollow()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        # Verificar si el usuario actual es el dueño del perfil
        context["is_owner"] = self.request.user == profile.user
        return context

    def follow(self):
        obj = self.get_object().user
        user = self.request.user
        user.following.add(obj)
        user.save()

    def unfollow(self):
        obj = self.get_object().user
        user = self.request.user
        user.following.remove(obj)
        user.save()


"""    def get(self, request, *args, **kwargs):
        user_id = kwargs.get(
            "pk"
        )  # Obtén el ID del perfil desde los parámetros de la URL
        try:
            profile = Profile.objects.get(id=user_id)
        except Profile.DoesNotExist:
            return redirect(reverse_lazy("home"))
        if profile.user.id == self.request.user.id or self.request.user.is_superuser:
            # Si es el propietario, realiza la acción normal del método get
            return super().get(request, *args, **kwargs)
        else:
            # Si no es el propietario, redirige a la página de inicio
            return redirect(reverse_lazy("home"))"""


@method_decorator(login_required, name="dispatch")
class ProfileUpdate(UpdateView):
    form_class = UserFormPro
    template_name = "registration/profile_update.html"

    def get_success_url(self) -> str:
        return reverse_lazy("profile", kwargs={"pk": self.request.user.profile.id})

    def get_object(self):
        return User.objects.get(pk=self.request.user.id)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["username"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
        form.fields["first_name"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
        form.fields["last_name"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
        form.fields["email"].widget = forms.EmailInput(attrs={"class": "form-control"})

        return form


@method_decorator(login_required, name="dispatch")
class BioUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "registration/bio_update.html"

    def get_object(self):
        return ProfileForm.Meta.model.objects.get(pk=self.request.user.profile.id)

    def get_success_url(self) -> str:
        return reverse_lazy("profile", kwargs={"pk": self.request.user.profile.id})

    def get_initial(self) -> dict[str, Any]:
        initial = super().get_initial()
        initial["user"] = self.request.user
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["user"].widget = forms.HiddenInput()
        return form


@method_decorator(login_required, name="dispatch")
class ImageUpdate(UpdateView):
    form_class = UserFormImage
    template_name = "registration/image_update.html"

    def get_success_url(self) -> str:
        return reverse_lazy("profile", kwargs={"pk": self.request.user.profile.id})

    def get_object(self):
        return User.objects.get(pk=self.request.user.id)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["image"].widget = forms.FileInput()
        return form

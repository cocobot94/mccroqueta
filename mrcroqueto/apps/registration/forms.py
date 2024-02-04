from django import forms
from apps.users.models import User
from apps.registration.models import Profile

from .models import Profile
from apps.users.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["user", "bio"]


class UserFormPro(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "email" in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email already exists")
        return email


class UserFormImage(forms.ModelForm):
    class Meta:
        model = User
        fields = ["image"]

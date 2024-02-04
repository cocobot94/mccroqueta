from django import forms
from apps.blog.models import Post, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "content", "image", "category_post"]
        """widgets = {
            "author": forms.HiddenInput(),
            "title": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "content": forms.Textarea(attrs={"class": "form-control mb-3"}),
            "image": forms.ClearableFileInput(),
            "category_post": forms.RadioSelect(),
        }"""


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["post", "user", "content"]

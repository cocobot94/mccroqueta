from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from apps.blog.forms import PostForm, CommentsForm
from django import forms

from apps.blog.models import Post, Comments


# Create your views here.

#
# Posts CRUD
#


# post list
@method_decorator(login_required, name="dispatch")
class PostViewSet(ListView):
    model = Post
    template_name = "blog/post.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(state=True)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["amount_revissions"] = Post.objects.filter(state=False).count()
        return context


@method_decorator(login_required, name="dispatch")
class PostsFavoritesViewSet(ListView):
    model = Post
    template_name = "blog/posts_favorites.html"
    context_object_name = "posts"

    def get_queryset(self):
        return self.request.user.favoritos.all()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["amount_revissions"] = Post.objects.filter(state=False).count()
        return context


# post detail view
@method_decorator(login_required, name="dispatch")
class PostDetailView(DetailView):
    template_name = "blog/post_detail.html"
    model = Post

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["comments"] = Comments.objects.filter(post=self.get_object().pk)
        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        if f"vista_post_{self.object.pk}" not in self.request.session:
            self.object.aumentar_vistas()
            self.request.session["vista_post_{}".format(self.object.pk)] = True
        # recibiendo desde el template el like y el dislike

        return super().get(request, *args, **kwargs)

    def like(self, obj, user):
        if user in obj.dislike.all():
            obj.dislike.remove(user)
        obj.like.add(user)
        obj.save()

    def nolikes(self, obj, user):
        obj.like.remove(user)
        obj.save()

    def dislike(self, obj, user):
        if user in obj.like.all():
            obj.like.remove(user)
        obj.dislike.add(user)
        obj.save()

    def nodislikes(self, obj, user):
        obj.dislike.remove(user)
        obj.save()

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user

        if request.POST.get("like"):
            self.like(post, user)
        elif request.POST.get("nolike"):
            self.nolikes(post, user)
        elif request.POST.get("dislike"):
            self.dislike(post, user)
        elif request.POST.get("nodislike"):
            self.nodislikes(post, user)
        elif request.POST.get("fav"):
            post.fav.add(user)
        elif request.POST.get("nofav"):
            post.fav.remove(user)
        return redirect(
            reverse_lazy("post_detail", kwargs={"pk": self.get_object().pk})
        )


@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_initial(self) -> dict[str, Any]:
        initial = super().get_initial()
        initial["author"] = self.request.user
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["author"].widget = forms.HiddenInput()
        form.fields["title"].widget = forms.TextInput(
            attrs={"class": "form-control mb-3"}
        )
        form.fields["content"].widget = forms.Textarea(
            attrs={"class": "form-control mb-3"}
        )
        form.fields["image"].widget = forms.ClearableFileInput()

        return form

    def get_success_url(self) -> str:
        return reverse_lazy("posts") + "?create"


@method_decorator(login_required, name="dispatch")
class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content", "image", "category_post"]
    template_name = "blog/post_update.html"

    def get_success_url(self) -> str:
        post = self.get_object()
        post.state = False
        post.save()
        return reverse_lazy("post_detail", kwargs={"pk": self.get_object().id})


@method_decorator(login_required, name="dispatch")
class PostDeleteView(DeleteView):
    template_name = "blog/post_delete.html"
    model = Post

    def get_success_url(self) -> str:
        return reverse_lazy("posts") + "?deleted"


#
# Posts revission
#
@method_decorator(login_required, name="dispatch")
class PostRevissionViewSet(ListView):
    model = Post
    template_name = "blog/post_revission.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(state=False)


# Revision Post detail
@method_decorator(login_required, name="dispatch")
class PostDetailRevissionView(UpdateView):
    template_name = "blog/post_detail_revission.html"
    model = Post
    fields = ["state", "title", "content", "image", "author", "category_post"]

    def get_success_url(self) -> str:
        post = self.get_object()
        if post.state == True:
            return reverse_lazy("posts") + "?ok"
        else:
            post.delete()
            return reverse_lazy("posts") + "?nop"


#
# posts category and author
#
@method_decorator(login_required, name="dispatch")
class PostCategoryViewSet(ListView):
    model = Post
    template_name = "blog/post_category.html"
    context_object_name = "posts"

    def get_queryset(self):
        category = self.kwargs["pk"]
        return Post.objects.filter(state=True, category_post=category)


#
# Comments
#


# comment list
@method_decorator(login_required, name="dispatch")
class CommentsListView(ListView):
    model = Comments
    template_name = "blog/comments.html"
    context_object_name = "comments"

    def get_queryset(self) -> QuerySet[Any]:
        obj = self.kwargs["pk"]
        return Comments.objects.filter(post=obj)


# Comment create
@method_decorator(login_required, name="dispatch")
class CommentsCreate(CreateView):
    model = Comments
    form_class = CommentsForm
    template_name = "blog/comment_create.html"

    def get_initial(self):
        initial = super().get_initial()
        initial["user"] = self.request.user
        initial["post"] = Post.objects.get(pk=self.kwargs["pk"])
        return initial

    def get_success_url(self) -> str:
        form = self.get_form()
        return reverse_lazy("post_detail", kwargs={"pk": form.instance.post.id})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["user"].widget = forms.HiddenInput()
        form.fields["post"].widget = forms.HiddenInput()
        form.fields["content"].widget = forms.Textarea(
            attrs={"class": "forms-control mb-3"}
        )
        return form

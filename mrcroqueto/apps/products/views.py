from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django import forms
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from apps.products.models import (
    Products,
    Order,
    OrderDetail,
    Indicator,
    CategoryProduct,
)
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from apps.products.forms import ProductsForm, OrderForm, DetailForm
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.db.models import Q


# @method_decorator(login_required, name="dispatch")


# Create your views here.
@method_decorator(login_required, name="dispatch")
class ListProducts(ListView):
    model = Products
    template_name = "products/offers.html"

    def get_queryset(self) -> QuerySet[Any]:
        categorias_indicator = CategoryProduct.objects.filter(categories__isnull=False)
        queryset = Products.objects.filter(category_product__in=categorias_indicator)
        return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["products"] = self.get_queryset()
        context["indicators"] = Indicator.objects.all()
        context["categories"] = CategoryProduct.objects.all()
        return context


@method_decorator(login_required, name="dispatch")
class MenuListView(ListView):
    model = Products
    template_name = "products/menu.html"
    context_object_name = "products"

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.filter(state=True)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["indicators"] = Indicator.objects.all()
        context["categories"] = CategoryProduct.objects.all()
        params = self.request.GET.get("search")
        products = self.get_queryset()
        if params:
            products = products.filter(
                Q(name__icontains=params) | Q(description__icontains=params)
            )
        context[self.context_object_name] = products
        return context


@method_decorator(login_required, name="dispatch")
class GalleryTemplateView(ListView):
    model = Products
    context_object_name = "products"
    template_name = "products/gallery.html"


@method_decorator(login_required, name="dispatch")
class ProductDetailView(DetailView):
    template_name = "products/product_info.html"
    model = Products

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryProduct.objects.all()
        return context


@method_decorator(login_required, name="dispatch")
class CreateProduct(CreateView):
    template_name = "products/create_product.html"
    form_class = ProductsForm

    def get_success_url(self) -> str:
        return reverse_lazy("product_info", kwargs={"pk": self.object.pk})


@method_decorator(login_required, name="dispatch")
class DeleteProduct(DeleteView):
    model = Products
    template_name = "products/products_confirm_delete.html"

    def get_success_url(self) -> str:
        return reverse_lazy("menu") + "?ok"


@method_decorator(login_required, name="dispatch")
class UpdateProduct(UpdateView):
    model = Products
    form_class = ProductsForm
    template_name = "products/update_product.html"

    def get_success_url(self) -> str:
        return reverse_lazy("product_info", args=[self.object.id]) + "?updated"


@method_decorator(login_required, name="dispatch")
class OrderView(DetailView):
    model = Order
    template_name = "products/order.html"


@method_decorator(login_required, name="dispatch")
class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "products/order_create.html"

    def get_success_url(self) -> str:
        return reverse_lazy("order", kwargs={"pk": self.request.user.user_orders.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["user"].widget = forms.HiddenInput()
        # form.fields["order_detail"].widget = forms.CheckboxSelectMultiple()
        form.fields["total"].widget = forms.HiddenInput()
        return form

    def get_object(self, queryset=None):
        # Si la orden ya existe, devuelve la instancia existente
        if self.kwargs.get("pk"):
            return get_object_or_404(
                Order, pk=self.kwargs["pk"], user=self.request.user
            )
        else:
            return None

    def form_invalid(self, form):
        # Manejar lógica específica en caso de formulario inválido
        return self.render_to_response(self.get_context_data(form=form))


@method_decorator(login_required, name="dispatch")
class OrderUpdate(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "products/order_update.html"

    def get_success_url(self):
        return reverse_lazy("order", kwargs={"pk": self.get_object()}) + "?actualizado"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["user"].widget = forms.HiddenInput()
        # form.fields["order_detail"].widget = forms.CheckboxSelectMultiple()
        form.fields["total"].widget = forms.HiddenInput()
        return form

    def get_object(self):
        order, created = Order.objects.get_or_create(
            pk=self.request.user.user_orders.pk
        )
        return order


@method_decorator(login_required, name="dispatch")
class OrderDeleteView(DeleteView):
    model = Order
    template_name = "products/order_delete.html"

    def get_success_url(self) -> str:
        return reverse_lazy("menu") + "?deleted"


@method_decorator(login_required, name="dispatch")
class DetailCreate(CreateView):
    model = OrderDetail
    form_class = DetailForm
    template_name = "products/detail_create.html"

    def get_success_url(self) -> str:
        try:
            order = Order.objects.get(pk=self.request.user.user_orders.id)
            return reverse_lazy("order_update", kwargs={"pk": order.id})
        except Order.DoesNotExist:
            return reverse_lazy("order_create")


@method_decorator(login_required, name="dispatch")
class CheckOutView(TemplateView):
    template_name = "products/check_out.html"


@method_decorator(login_required, name="dispatch")
class MenuCategoryListView(ListView):
    model = Products
    template_name = "products/menu_category.html"
    context_object_name = "products"

    def get_queryset(self) -> QuerySet[Any]:
        obj = self.kwargs["pk"]
        queryset = Products.objects.filter(state=True, category_product=obj)
        return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["indicators"] = Indicator.objects.all()
        context["categories"] = CategoryProduct.objects.all()
        return context

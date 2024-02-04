from django import forms
from .models import Products, Order, OrderDetail


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["name", "image", "description", "price", "menu", "category_product"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(),
            "menu": forms.RadioSelect(),
            "category_product": forms.RadioSelect(),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {
            "order_detail": forms.CheckboxSelectMultiple(),
        }


class DetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = "__all__"

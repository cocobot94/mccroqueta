from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField
from apps.users.models import User
from django.urls import reverse_lazy

from django.db.models.signals import m2m_changed, post_save, pre_delete, pre_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404


def custom_upload_to(instance, filename):
    try:
        old_instance = Products.objects.get(pk=instance.pk)
        old_instance.image.delete()
        return "products/" + filename
    except Products.DoesNotExist:
        return "products/" + filename


# Create your models here.


class CategoryProduct(models.Model):
    description = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.description


class Products(models.Model):
    choices = [
        ("breakfast", "BREAKFAST"),
        ("lunch", "LUNCH"),
        ("dinner", "DINNER"),
        ("happy_hour", "HAPPY_HOUR"),
        ("all_day", "ALL_DAY"),
    ]
    name = models.CharField(max_length=50, unique=True)
    state = models.BooleanField(default=True)
    description = RichTextField()
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=custom_upload_to)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    old_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    menu = models.CharField(max_length=50, choices=choices, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    """def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            # Redimensionar la imagen a 300x300 pixeles
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        super().save(*args, **kwargs)"""

    def calculate_price_indicator(self):
        self.old_price = self.price
        if self.category_product.categories.exists():
            indicator = self.category_product.categories.first()
            self.price -= self.old_price * indicator.value
        return self.price

    def delete_indicator(self):
        if self.category_product.categories.exists():
            indicator = self.category_product.categories.first()
            self.price += self.old_price * indicator.value
        return self.price

    def __str__(self) -> str:
        return self.name


class Indicator(models.Model):
    category_product = models.ForeignKey(
        CategoryProduct, on_delete=models.CASCADE, related_name="categories"
    )
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f"{int(self.value * 100)}%"


class OrderDetail(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.amount} - {self.product.name} "


class Order(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="user_orders",
    )
    order_detail = models.ManyToManyField(OrderDetail)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cant = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.id)

    def calculate_total(self):
        self.total = sum(
            item.product.price * item.amount for item in self.order_detail.all()
        )
        return self.total

    def cantidad(self):
        self.cant = self.order_detail.count()
        return self.cant


# sender: Es el modelo que envía la señal.
# En este caso, es la clase Order.order_detail.through,
# que representa la tabla intermedia generada automáticamente para la relación muchos a muchos.
# action: Es un string que indica la acción que activó la señal. Puede ser "pre_add"
@receiver(m2m_changed, sender=Order.order_detail.through)
def update_total(sender, instance, action, **kwargs):
    if action in ("post_add", "post_remove", "post_clear"):
        instance.calculate_total()
        instance.cantidad()
        instance.save()


@receiver(post_save, sender=Indicator)
def update_price(sender, instance, **kwargs):
    if kwargs.get("created"):
        # Obtener todos los productos relacionados con la categoría del indicador
        related_products = Products.objects.filter(
            category_product=instance.category_product
        )
        # Actualizar el precio en todos los productos relacionados
        for product in related_products:
            product.calculate_price_indicator()
            product.save()


@receiver(pre_save, sender=Indicator)
def no_act_price(sender, instance, **kwargs):
    if instance.pk:
        raise Exception("error no puede act el indicador")


@receiver(pre_delete, sender=Indicator)
def update_price(sender, instance, **kwargs):
    # Obtener todos los productos relacionados con la categoría del indicador
    related_products = Products.objects.filter(
        category_product=instance.category_product
    )

    # Actualizar el precio en todos los productos relacionados
    for product in related_products:
        product.delete_indicator()
        product.save()


"""@receiver(pre_save, sender=Order)
def update_order_view(sender, instance, **kwargs):
    if not kwargs.get("created"):
        # Recupera la instancia existente de la orden
        existing_order = get_object_or_404(Order, id=instance.id)

        # Actualiza campos regulares si es necesario
        # existing_order.algun_campo = instance.algun_campo
        # ...

        # Actualiza campos ManyToMany utilizando el método set
        existing_order.order_detail.set(instance.order_detail.all())

        # Guarda la instancia actualizada
        existing_order.save()
"""

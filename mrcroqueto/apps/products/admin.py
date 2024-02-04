from django.contrib import admin
from .models import Products, CategoryProduct, OrderDetail, Order, Indicator
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class ProductsResources(resources.ModelResource):
    class Meta:
        model = Products


class CategoryResources(resources.ModelResource):
    class Meta:
        model = CategoryProduct


class ProductsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("name", "price", "category_product")
    search_fields = ["name"]
    resource_class = ProductsResources

    """def get_category(self, obj):
        return ", ".join(
            categories.description for categories in obj.category_product.all()
        )

    get_category.short_description = "category"
    """


class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["description"]
    resource_class = CategoryResources


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "id", "total")


class IndicatorAdmin(admin.ModelAdmin):
    list_display = ("category_product", "get_value_str")

    def get_value_str(self, obj):
        return str(obj)

    get_value_str.short_description = "Indicator"


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ("product", "amount")


admin.site.register(Products, ProductsAdmin)
admin.site.register(CategoryProduct, CategoryAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Indicator, IndicatorAdmin)

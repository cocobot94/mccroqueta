from django.urls import path
from apps.products.views import (
    ListProducts,
    MenuListView,
    GalleryTemplateView,
    ProductDetailView,
    CreateProduct,
    DeleteProduct,
    UpdateProduct,
    OrderView,
    OrderCreate,
    OrderUpdate,
    DetailCreate,
    CheckOutView,
    OrderDeleteView,
    MenuCategoryListView,
)


urlpatterns = [
    path("offers/", ListProducts.as_view(), name="offers"),
    path("menu/", MenuListView.as_view(), name="menu"),
    path("gallery/", GalleryTemplateView.as_view(), name="gallery"),
    path("product_info/<int:pk>/", ProductDetailView.as_view(), name="product_info"),
    path("product_create/", CreateProduct.as_view(), name="create_product"),
    path("delete/<int:pk>/", DeleteProduct.as_view(), name="delete_product"),
    path("update/<int:pk>/", UpdateProduct.as_view(), name="update_product"),
    path("order/<int:pk>/", OrderView.as_view(), name="order"),
    path("order/create/", OrderCreate.as_view(), name="order_create"),
    path("order/update/<int:pk>/", OrderUpdate.as_view(), name="order_update"),
    path("order/detail_create/", DetailCreate.as_view(), name="detail_create"),
    path("order/check_out/", CheckOutView.as_view(), name="check_out"),
    path("order/delete/<int:pk>/", OrderDeleteView.as_view(), name="order_delete"),
    path(
        "menu_category/<int:pk>/", MenuCategoryListView.as_view(), name="menu_category"
    ),
]

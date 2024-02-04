from rest_framework import viewsets
from apps.api.serializers.product_serializer import (
    ProductSerializer,
    OrderSerializer,
    OrderDetailSerializer,
    IndicatorSerializer,
    CategoryProductSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)


class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()


class OrderDetailViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

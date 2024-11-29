# products/api_views.py
from rest_framework import viewsets
from .models import Products, Variant, SubVariant
from .serializers import ProductSerializer, VariantSerializer, SubVariantSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class VariantViewSet(viewsets.ModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer

class SubVariantViewSet(viewsets.ModelViewSet):
    queryset = SubVariant.objects.all()
    serializer_class = SubVariantSerializer

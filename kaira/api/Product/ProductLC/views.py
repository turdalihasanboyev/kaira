from rest_framework.generics import ListCreateAPIView

from kaira.models import Product
from .serializers import ProductLCAPISerializer


class ProductLCAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductLCAPISerializer

    def get_queryset(self):
        queryset = self.queryset.select_related('category')
        return queryset

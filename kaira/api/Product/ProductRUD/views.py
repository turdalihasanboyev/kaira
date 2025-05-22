from rest_framework.generics import RetrieveUpdateDestroyAPIView

from kaira.models import Product
from .serializers import ProductRUDAPISerializer


class ProductRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRUDAPISerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = self.queryset.select_related('category')
        return queryset

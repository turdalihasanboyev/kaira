from rest_framework.generics import RetrieveUpdateDestroyAPIView

from kaira.models import Category
from .serializers import CategoryRUDAPISerializer


class CategoryRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRUDAPISerializer
    lookup_field = 'pk'

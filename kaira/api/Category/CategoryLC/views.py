from rest_framework.generics import ListCreateAPIView

from kaira.models import Category
from .serializers import CategoryLCAPISerializer


class CategoryLCAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryLCAPISerializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from kaira.models import Blog
from .serializers import BlogRUDAPISerializer


class BlogRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogRUDAPISerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = self.queryset.select_related('category')
        return queryset

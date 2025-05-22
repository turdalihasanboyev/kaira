from rest_framework.generics import ListCreateAPIView

from kaira.models import Blog
from .serializers import BlogLCAPISerializer


class BlogLCAPIView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogLCAPISerializer

    def get_queryset(self):
        queryset = self.queryset.select_related('category')
        return queryset

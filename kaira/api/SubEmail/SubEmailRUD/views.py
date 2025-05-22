from rest_framework.generics import RetrieveUpdateDestroyAPIView

from kaira.models import SubEmail
from .serializers import SubEmailRUDAPISerializer


class SubEmailRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SubEmail.objects.all()
    serializer_class = SubEmailRUDAPISerializer
    lookup_field = 'pk'

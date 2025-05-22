from rest_framework.generics import ListCreateAPIView

from kaira.models import SubEmail
from .serializers import SubEmailLCAPISerializer


class SubEmailLCAPIView(ListCreateAPIView):
    queryset = SubEmail.objects.all()
    serializer_class = SubEmailLCAPISerializer

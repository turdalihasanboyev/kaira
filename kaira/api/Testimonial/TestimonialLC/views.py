from rest_framework.generics import ListCreateAPIView

from kaira.models import Testimonial
from .serializers import TestimonialLCAPISerializer


class TestimonialLCAPIView(ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialLCAPISerializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from kaira.models import Testimonial
from .serializers import TestimonialRUDAPISerializer


class TestimonialRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialRUDAPISerializer
    lookup_field = 'pk'

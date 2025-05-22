from rest_framework.serializers import ModelSerializer

from kaira.models import Testimonial


class TestimonialRUDAPISerializer(ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

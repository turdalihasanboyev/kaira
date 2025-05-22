from rest_framework.serializers import ModelSerializer

from kaira.models import Product


class ProductLCAPISerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

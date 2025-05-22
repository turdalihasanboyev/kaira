from rest_framework.serializers import ModelSerializer

from kaira.models import Category


class CategoryLCAPISerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

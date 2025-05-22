from rest_framework.serializers import ModelSerializer

from kaira.models import Category


class CategoryRUDAPISerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

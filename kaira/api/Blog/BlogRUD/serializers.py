from rest_framework.serializers import ModelSerializer

from kaira.models import Blog


class BlogRUDAPISerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

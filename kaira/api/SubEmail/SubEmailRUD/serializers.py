from rest_framework.serializers import ModelSerializer

from kaira.models import SubEmail


class SubEmailRUDAPISerializer(ModelSerializer):
    class Meta:
        model = SubEmail
        fields = '__all__'

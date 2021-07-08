from rest_framework import serializers
from core.models import Trabajo

class TrabajoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trabajo
        fields = '__all__'
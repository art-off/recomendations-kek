from rest_framework import serializers
from .models import Recomendation

class RecomendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendation
        fields = '__all__'

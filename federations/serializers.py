from rest_framework import serializers
from .models import Federation, PlayerProfile

class FederationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Federation
        fields = '__all__'

class PlayerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerProfile
        fields = '__all__'

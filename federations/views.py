from rest_framework import viewsets
from .models import Federation, PlayerProfile
from .serializers import FederationSerializer, PlayerProfileSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class FederationViewSet(viewsets.ModelViewSet):
    queryset = Federation.objects.all()
    serializer_class = FederationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class PlayerProfileViewSet(viewsets.ModelViewSet):
    queryset = PlayerProfile.objects.all()
    serializer_class = PlayerProfileSerializer
    permission_classes = [IsAuthenticated]

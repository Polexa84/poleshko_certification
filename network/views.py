from rest_framework import viewsets
from .models import Network, Product
from .serializers import NetworkSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsActiveEmployee

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]

class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    permission_classes = [IsActiveEmployee]
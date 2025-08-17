from rest_framework import serializers
from .models import Network, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'  # Или укажи конкретные поля, которые хочешь сериализовать
        read_only_fields = ('debt', 'level')  # Запрещаем изменение поля debt и level через API
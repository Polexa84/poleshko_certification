from django.urls import path, include
from rest_framework import routers
from .views import NetworkViewSet, ProductViewSet # добавил ProductViewSet

router = routers.DefaultRouter()
router.register(r'network', NetworkViewSet) #регистрируем NetworkViewSet
router.register(r'product', ProductViewSet) #регистрируем ProductViewSet

urlpatterns = [
    path('', include(router.urls)),
]
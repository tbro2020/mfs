from rest_framework.routers import DefaultRouter
from core import viewsets

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'products', viewsets.ProductViewSet, basename="products")
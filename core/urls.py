from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EntityViewSet

router = DefaultRouter()
router.register(r'entity', EntityViewSet, basename='provider')

urlpatterns = [
    path('', include(router.urls)),
]

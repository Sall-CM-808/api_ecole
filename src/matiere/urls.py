from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MatiereViewsSet

router = DefaultRouter()
router.register(r'matieres', MatiereViewsSet)

urlpatterns = [
    path('', include(router.urls))
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EvaluationViewsSet

router = DefaultRouter()
router.register(r'evaluations', EvaluationViewsSet)

urlpatterns = [
    path('', include(router.urls))
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClasseViewsSet

router = DefaultRouter()
router.register(r'classes', ClasseViewsSet)

urlpatterns = [
    path('', include(router.urls))
]

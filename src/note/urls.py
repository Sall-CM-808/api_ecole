from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NoteViewsSet

router = DefaultRouter()
router.register(r'notes', NoteViewsSet)

urlpatterns = [
    path('', include(router.urls))
]
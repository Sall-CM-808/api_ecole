from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NoteCoursViewsSet, NoteComposViewsSet

router = DefaultRouter()
router.register(r'notesCours', NoteCoursViewsSet)
router.register(r'notesCompos', NoteComposViewsSet)

urlpatterns = [
    path('', include(router.urls))
]
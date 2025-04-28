from django.urls import path
from tutor import views

urlpatterns = [
    path('create',views.TutorMixin.as_view(),name='tutor_create'),
    path('show/<int:pk>',views.TutorMixin.as_view(),name='show_tutor'),
    path('list',views.TutorMixin.as_view(),name='show_all_tutors'),
    path('delete/<int:pk>',views.TutorMixin.as_view(),name='delete_tutor'),
    path('update/<int:pk>',views.TutorMixin.as_view(),name='update_tutor'),
]

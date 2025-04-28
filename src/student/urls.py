from django.urls import path
from student import views

urlpatterns = [
    path('create',views.StudentMixin.as_view(),name='create_student'),
    path('show/<int:pk>',views.StudentMixin.as_view(),name='shwo_student'),
    path('delete/<int:pk>',views.StudentMixin.as_view(),name='delete_student'),
    path('list',views.StudentMixin.as_view(),name='student_list'),
    path('update/<int:pk>',views.StudentMixin.as_view(),name='update_student'),
]

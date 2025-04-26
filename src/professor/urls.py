from django.urls import path
from professor import views

urlpatterns = [
    path('create',views.ProfessorMixin.as_view(),name='create_professor'),
    path('show/<int:pk>',views.ProfessorMixin.as_view(),name='show_professor'),
    path('list',views.ProfessorMixin.as_view(),name='list_professor'),
    path('delete/<int:pk>',views.ProfessorMixin.as_view(),name='delete_professor'),
]

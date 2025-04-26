from django.urls import path
from manager import views

urlpatterns = [
    path('create',views.SchoolManagerMixin.as_view(),name='create_manager'),
    path('show/<int:pk>',views.SchoolManagerMixin.as_view(),name='show_manager'),
    path('list',views.SchoolManagerMixin.as_view(),name='list_manager'),
    path('delete/<int:pk>',views.SchoolManagerMixin.as_view(),name='delete_manager'),
]

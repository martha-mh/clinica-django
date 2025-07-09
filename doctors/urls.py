from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.list_doctors, name='list_doctors'),
    path('doctors/delete/<int:pk>/', views.delete_doctor, name='delete_doctor'),
    path('doctors/create/', views.create_doctor, name='create_doctor'),
    path('doctors/edit/<int:pk>/', views.edit_doctor, name='edit_doctor'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_appointments, name='list_appointments'),
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('appointments/create/', views.create_appointment, name='create_appointment'),
    path('appointments/edit/<int:pk>/', views.edit_appointment, name='edit_appointment'),
    path('appointments/delete/<int:pk>/', views.delete_appointment, name='delete_appointment'),
    path('appointments/reset/<int:pk>/', views.reset_appointment, name='reset_appointment'),
    path('appointments/list_deleted/', views.list_appointments_deleted, name='list_appointments_deleted'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.list_patients, name='list_patients'),
    path('patients/delete/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('patients/create/', views.create_patient, name='create_patient'),
    path('patients/edit/<int:pk>/', views.edit_patient, name='edit_patient'),
]
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from patients import models
from .models import Patient
from django.contrib import messages
from .forms import PatientForm
from django.db.models import ProtectedError

# Vistas frontend clásicas

@login_required
def list_patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients/list.html', {'patients': patients})

@login_required
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    try:
        patient.delete()
        messages.success(request, 'Paciente eliminado exitosamente.')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar porque tiene citas registradas.')
    return redirect('list_patients')

@login_required
def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            messages.success(request, 'Paciente creado exitosamente.')
            return redirect('list_patients')
    else:
        form = PatientForm()
    return render(request, 'patients/form.html', {'form': form})

@login_required
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente editado exitosamente.')
            return redirect('list_patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/form.html', {'form': form, 'edit': True})

# Vistas API DRF

from rest_framework import viewsets, permissions
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
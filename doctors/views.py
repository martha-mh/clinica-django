from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from doctors import models
from .models import Doctor
from django.contrib import messages
from .forms import DoctorForm
from django.db.models import ProtectedError

# Vistas frontend clásicas

@login_required
def list_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/list.html', {'doctors': doctors})

@login_required
def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    try:
        doctor.delete()
        messages.success(request, 'Doctor eliminado exitosamente.')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar porque tiene citas registradas.')
    return redirect('list_doctors')

@login_required
def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save()
            messages.success(request, 'Doctor creado exitosamente.')
            return redirect('list_doctors')
    else:
        form = DoctorForm()
    return render(request, 'doctors/form.html', {'form': form})

@login_required
def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor editado exitosamente.')
            return redirect('list_doctors')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/form.html', {'form': form, 'edit': True})


# Vistas API DRF

from rest_framework import viewsets, permissions
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

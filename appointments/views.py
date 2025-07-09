from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from django.contrib import messages
from .forms import AppointmentForm

# Vistas frontend clásicas

@login_required
def list_appointments(request):
    appointments = Appointment.objects.filter(eliminated=False)
    return render(request, 'appointments/list.html', {'appointments': appointments})

@login_required
def list_appointments_deleted(request):
    appointments = Appointment.objects.filter(eliminated=True)
    return render(request, 'appointments/list_deleted.html', {'appointments': appointments})

@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            messages.success(request, 'Cita creada exitosamente.')
            return redirect('list_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/form.html', {'form': form})

@login_required
def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cita editada exitosamente.')
            return redirect('list_appointments')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/form.html', {'form': form, 'edit': True})


@login_required
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.eliminated = True
    appointment.save()
    messages.success(request, 'Cita eliminada exitosamente.')
    return redirect('list_appointments')

@login_required
def reset_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.eliminated = False
    appointment.save()
    messages.success(request, 'Cita restablecida exitosamente.')
    return redirect('list_appointments_deleted')


# Vistas API DRF

from rest_framework import viewsets, permissions
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
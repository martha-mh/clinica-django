from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    date_time = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    type = models.CharField(max_length=50)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    number = models.CharField(
        max_length=20,
        unique=True,
        error_messages={
            'unique': 'Ya existe una cita con este número.'
        }
    )
    eliminated = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_time']

    def __str__(self):
        return f"Appointment {self.number} - {self.patient}"
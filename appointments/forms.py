from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = ['eliminated']
        fields = ['date_time', 'patient', 'type', 'doctor', 'number']
        labels = {
            'date_time': 'Fecha y hora',
            'patient': 'Paciente',
            'type': 'Tipo de cita',
            'doctor': 'Doctor',
            'number': 'Número de cita'
        }
        widgets = {
            'date_time': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local'
                },
                format='%Y-%m-%dT%H:%M'
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control m-5'
            field.widget.attrs['required'] = 'required'

        # en la edición, hacer que los campos 'number' y 'patient' sean de solo lectura
        if self.instance and self.instance.pk:
            self.fields['number'].widget.attrs['readonly'] = True
            self.fields['patient'].widget.attrs['disabled'] = True
from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialty']
        labels = {
            'name': 'Nombre',
            'specialty': 'Especialidad'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control m-5'
            field.widget.attrs['required'] = 'required'
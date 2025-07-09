from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'phone']
        labels = {
            'name': 'Nombre',
            'email': 'Email',
            'phone': 'Teléfono'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control m-5'
            field.widget.attrs['required'] = 'required'
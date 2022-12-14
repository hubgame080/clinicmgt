from django.forms import ModelForm
from django import forms
from .models import Patient

class PatientForm(ModelForm):
    birth_day = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y'],
        
    )

    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'birth_day': forms.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_day'].label = "BIRTH DAY (DD/MM/YYY)"
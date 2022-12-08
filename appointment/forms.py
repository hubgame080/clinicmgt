from datetime import date
from django.forms import ModelForm
from .models import Appointment
from django import forms

class AppointmentForm(ModelForm):
    set_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=date.today)
    set_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))


    class Meta:
        model = Appointment
        fields = '__all__'
        exclude = [
         
            'status'
        ]
       
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['set_date'].required = False
        self.fields['set_time'].required = False
        
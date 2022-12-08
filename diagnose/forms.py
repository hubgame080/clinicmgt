from django.forms import ModelForm
from .models import Diagnose
from django import forms

class DiagnoseForm(ModelForm):
    examine = forms.CharField(widget=forms.Textarea(attrs={'style': 'height: 500px'}))
    prescription = forms.CharField(widget=forms.Textarea(attrs={'style': 'height: 100px'}))

    class Meta:
        model = Diagnose
        fields = '__all__'
        exclude = [
            'patient',
            'appointment'
        ]
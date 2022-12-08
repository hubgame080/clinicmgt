from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
from patient.models import Patient

class Appointment(models.Model):
    STATUS = [
        ("1", "Complete"), 
        ("2", "Ongoing")
    ]

    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    set_time =  models.TimeField(blank=True, null=True, default='')
    set_date = models.DateField(blank=True, null=True, default='')
    status = models.CharField(max_length=20, choices=STATUS, default='2')
    created_by = UserForeignKey(auto_user_add=True, related_name="Appointment")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.patient.last_name + ' ' +  self.patient.first_name + ', ' + self.patient.middle_name

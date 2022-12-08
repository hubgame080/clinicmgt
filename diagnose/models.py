from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
from patient.models import Patient
from appointment.models import Appointment

class Diagnose(models.Model):
    STATUS = [
        ("1", "Complete"), 
        ("2", "Ongoing")
    ]


    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True)
    weight =  models.CharField(max_length=20, blank=True, null=True, default='')
    height =  models.CharField(max_length=20, blank=True, null=True, default='')
    blood_pressure =  models.CharField(max_length=20, blank=True, null=True, default='')
    examine = models.TextField(blank=True, null=True, default='')
    prescription = models.TextField(blank=True, null=True, default='')
    status = models.CharField(max_length=20, choices=STATUS, default='2')
    created_by = UserForeignKey(auto_user_add=True, related_name="Daignose")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.patient.last_name + ' ' +  self.patient.first_name + ', ' + self.patient.middle_name

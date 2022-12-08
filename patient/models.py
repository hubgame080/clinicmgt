from django.db import models
from django_userforeignkey.models.fields import UserForeignKey


class Patient(models.Model):
    GENDER = [
        ("1", "Male"), 
        ("2", "Female")
    ]
    first_name = models.CharField(max_length=120, null=False, blank=False)
    middle_name = models.CharField(max_length=120, null=False, blank=False)
    last_name = models.CharField(max_length=120, null=False, blank=False)
    birth_day = models.DateField(max_length=120, null=False, blank=False)
    age = models.IntegerField()
    address = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(max_length=120, null=False, blank=False)
    gender = models.CharField(max_length=20, choices=GENDER, default='1')
    mobile_no = models.CharField(max_length=120, null=False, blank=False)
    created_by = UserForeignKey(auto_user_add=True, related_name="Patient")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def full_Name(self):
        return self.last_name + ' ' +  self.first_name + ', ' + self.middle_name

    def __str__(self):
        return self.last_name + ' ' +  self.first_name + ', ' + self.middle_name

class LastCheckup(models.Model):
    last_checkup = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.last_checkup.last_name + ' ' +  self.last_checkup.first_name + ', ' + self.last_checkup.middle_name
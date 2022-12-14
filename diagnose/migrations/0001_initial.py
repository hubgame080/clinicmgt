# Generated by Django 4.1.3 on 2022-12-08 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('height', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('blood_pressure', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('examine', models.TextField(blank=True, default='', null=True)),
                ('prescription', models.TextField(blank=True, default='', null=True)),
                ('status', models.CharField(choices=[('1', 'Complete'), ('2', 'Ongoing')], default='2', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointment.appointment')),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Daignose', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.patient')),
            ],
        ),
    ]

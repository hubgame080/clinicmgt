from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from appointment.models import Appointment
from patient.models import Patient
from .models import Diagnose
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import DiagnoseForm


import datetime


def save_data(request, form, template_name, model, template_list, msg):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            objModels = model.objects.all().order_by('-updated_at')
            data['html_list'] = render_to_string(template_list, {
                'objModels': objModels,
                'messages': msg
            })
           
        else:
            data['form_is_valid'] = False
    context = {'form': form }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def QueuingList(request):
    objModels = Appointment.objects.filter(set_date=datetime.date.today(), status='2').order_by('set_date', 'set_time')
    context = {
        'objModels': objModels,
        'PageName' : 'Today Queuing',
        
        }
    return render(request, 'diagnose/queuinglist.html', context)


def DiagnoseCreate(request, pk):
    sObj = get_object_or_404(Appointment, pk=pk)
    form = DiagnoseForm(request.POST or None)
  
    if request.method == 'POST':
        if form.is_valid():
            appointmet_status = Appointment.objects.get(id = sObj.id)    
            appointmet_status.status = '1'
            appointmet_status.save()

            form.instance.patient = Patient.objects.get(id=sObj.patient.id)
            form.instance.appointment = Appointment.objects.get(id=sObj.id)
            saveexamine = form.save(commit=False)
            saveexamine.save()

            context = {
                'form': form,
                'PageName' : 'Diagnose',
                'sObj': sObj,
                'messages': 'Data was saved!'
            }
            return render(request, "diagnose/create.html", context)

    context = {
        'form': form,
        'PageName' : 'Diagnose',
        'sObj': sObj,
       
    }
    return render(request, "diagnose/create.html", context)

def ExamineTodayList(request):
    objModels = Diagnose.objects.filter(created_at__date=datetime.date.today()).order_by('created_at')
    context = {
        'objModels': objModels,
        'PageName' : 'Today Examine',

        }
    return render(request, 'diagnose/examinelist.html', context)

def DiagnoseUpdate(request, pk):
    sObj = get_object_or_404(Diagnose, pk=pk)
    form = DiagnoseForm(request.POST or None , instance = sObj)
  
    if request.method == 'POST':
        if form.is_valid():
            appointmet_status = Appointment.objects.get(id = sObj.id)    
            appointmet_status.status = '1'
            appointmet_status.save()

            form.instance.patient = Patient.objects.get(id=sObj.patient.id)
            form.instance.appointment = Appointment.objects.get(id=sObj.id)
            saveexamine = form.save(commit=False)
            saveexamine.save()

            context = {
                'form': form,
                'PageName' : 'Diagnose',
                'sObj': sObj,  
                'messages': 'Data was saved!'
                }
            return render(request, "diagnose/update.html", context)
           
    context = {
        'form': form,
        'PageName' : 'Diagnose',
        'sObj': sObj,
    }
    return render(request, "diagnose/update.html", context)


def DaignoseList(request):
    objModels = Diagnose.objects.all().order_by('-created_at')
    context = {
        'objModels': objModels,
        'PageName' : 'Diagnose',
        
        }
    return render(request, 'diagnose/list.html', context)
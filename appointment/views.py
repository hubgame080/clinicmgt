from django.shortcuts import render, get_object_or_404
from .models import Appointment
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import AppointmentForm
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


def AppointmentList(request):
    objModels = Appointment.objects.all().order_by('-updated_at')
    context = {
        'objModels': objModels,
        'PageName' : 'Appointment',
        
        }
    return render(request, 'appointment/list.html', context)


def AppointmentCreate(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
    else:
        form = AppointmentForm
    return save_data(request, form, 'appointment/create.html', Appointment, 'appointment/obj_list.html', 'Data was saved!')

def AppointmentUpdate(request, pk):
    sObj = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=sObj)
    else:
        form = AppointmentForm(instance=sObj)
    return save_data(request, form, 'appointment/update.html', Appointment, 'appointment/obj_list.html', 'Data was updated!')


def AppointmentDelete(request, pk):
    sObj = get_object_or_404(Appointment, pk=pk)
    data = dict()
    if request.method == 'POST':
        sObj.delete()
        data['form_is_valid'] = True
        objModels = Appointment.objects.all().order_by('-updated_at')
        data['html_list'] = render_to_string('appointment/obj_list.html', {
            'objModels': objModels,
            'messages': 'Data was deleted!'
        })
    else:
        context = {'sObj': sObj}
        data['html_form'] = render_to_string('appointment/delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def AppointmentTodayList(request):
    objModels = Appointment.objects.filter(set_date=datetime.date.today(), status='2').order_by('set_date', 'set_time')
    context = {
        'objModels': objModels,
        'PageName' : 'Appointment for Today',
        
        }
    return render(request, 'appointment/list.html', context)
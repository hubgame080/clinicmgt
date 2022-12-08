from django.shortcuts import render, get_object_or_404
from .models import Patient
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import PatientForm


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


def PatientList(request):
    objModels = Patient.objects.all().order_by('-updated_at')
    context = {
        'objModels': objModels,
        'PageName' : 'Patient',
        
        }
    return render(request, 'patient/list.html', context)


def PatientCreate(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
    else:
        form = PatientForm
    return save_data(request, form, 'patient/create.html', Patient, 'patient/obj_list.html', 'Data was saved!')

def PatientUpdate(request, pk):
    sObj = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=sObj)
    else:
        form = PatientForm(instance=sObj)
    return save_data(request, form, 'patient/update.html', Patient, 'patient/obj_list.html', 'Data was updated!')


def PatientDelete(request, pk):
    sObj = get_object_or_404(Patient, pk=pk)
    data = dict()
    if request.method == 'POST':
        sObj.delete()
        data['form_is_valid'] = True
        objModels = Patient.objects.all().order_by('-updated_at')
        data['html_list'] = render_to_string('patient/obj_list.html', {
            'objModels': objModels,
            'messages': 'Data was deleted!'
        })
    else:
        context = {'sObj': sObj}
        data['html_form'] = render_to_string('patient/delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)
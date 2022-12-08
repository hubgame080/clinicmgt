from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.PatientList, name='patient-list'),
    path('create/', views.PatientCreate, name='patient-create'),
    path('<int:pk>/update', views.PatientUpdate, name='patient-update'),
    path('<int:pk>/delete', views.PatientDelete, name='patient-delete'),    
]

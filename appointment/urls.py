from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.AppointmentList, name='appointment-list'),
    path('create/', views.AppointmentCreate, name='appointment-create'),
    path('<int:pk>/update', views.AppointmentUpdate, name='appointment-update'),
    path('<int:pk>/delete', views.AppointmentDelete, name='appointment-delete'),
    path('today/', views.AppointmentTodayList, name='appointmenttoday-list'),    
    
]

from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('queuing/', views.QueuingList, name='queuing-list'),
    path('<int:pk>/create/', views.DiagnoseCreate, name='diagnose-create'),
    path('examine/today', views.ExamineTodayList, name='examinetoday-list'),
    path('<int:pk>/update', views.DiagnoseUpdate, name='examine-update'),
    path('list/', views.DaignoseList, name='diagnose-list'),  
    
    # path('create/', views.AppointmentCreate, name='appointment-create'),
    # path('<int:pk>/update', views.AppointmentUpdate, name='appointment-update'),
    # path('<int:pk>/delete', views.AppointmentDelete, name='appointment-delete'),
    # path('today/', views.AppointmentTodayList, name='appointmenttoday-list'),    
]

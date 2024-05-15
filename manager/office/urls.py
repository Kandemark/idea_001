
from django.urls import path
from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home, name='home'),  # Mapping the root URL to the home view
    path('employees/', views.employees, name='employees'),  # Mapping the '/employees/' URL to the employees view
    path('logout/', views.logout, name='logout'),  
    path('profile/', views.profile, name='profile'),  
    path('projects/', views.projects, name='projects'),  
    path('signin/', views.signin, name='signin'),  
    path('tasks/', views.tasks, name='tasks'), 
    path('employment-application/', views.employment_application, name='employment_application'), 
    path('success/', views.success_page, name='success_page'),
    path('employees/', views.employees, name='applications_review'),
    path('process-employees/', views.process_employees, name='process_employees'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),

    path('product/' ,views.productlist)
   
   # path('add', views.display_employees, name="add")
]

urlpatterns = format_suffix_patterns(urlpatterns)
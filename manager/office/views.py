
from django.contrib import messages
from .models import Applicant
from .forms import EmploymentApplicationForm
from .models import PromotedEmployee 
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm  
from .models import Task



# Create your views here.
#def home(request):
  #template = loader.get_template('home.html')
  #return HttpResponse(template.render())

def static(request):
    return render(request, 'styles.css')


def home(request):
    return render(request, 'home.html')
def tasks(request):
    return render(request, 'tasks.html')
def logout(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')
def projects(request):
    return render(request, 'projects.html')
def signin(request):
    return render(request, 'signin.html')
def tasks(request):
    return render(request, 'tasks.html')
def employees(request):
    return render(request, 'employees.html')
def success_page(request):
    return render(request, 'success_page.html')



def employees(request):
    pending_applications = Applicant.objects.filter(employment_status='Pending')
    
    for application in pending_applications:
        if application.years_of_experience is not None and application.education_level is not None:
            if application.years_of_experience >= 2 and application.education_level == 'Bachelor':
                application.employment_status = 'Approved'
                application.save()
                # Send a notification to the user
                messages.success(request, f'Congratulations, {application.firstname} {application.lastname}! Your application has been approved for employment.')
            else:
                application.employment_status = 'Rejected'
                application.save()
                # Send a notification to the user
                messages.warning(request, f'Sorry, {application.firstname} {application.lastname}. Your application does not meet the requirements for employment.')
        else:
            application.employment_status = 'Rejected'
            application.save()
            # Send a notification to the user
            messages.warning(request, f'Sorry, {application.firstname} {application.lastname}. Your application is incomplete and has been rejected.')
    
    applicants = Applicant.objects.all()
    return render(request, 'employees.html', {'employees': applicants})

def employment_application(request):
    if request.method == 'POST':
        form = EmploymentApplicationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('success_page')  
    else:
        form = EmploymentApplicationForm
    return render(request, 'employment_application.html', {'form': form})


def process_employees(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action:
            action_parts = action.split('_')
            if len(action_parts) == 2:
                action_type, employee_id = action_parts
                if action_type == 'del':
                    employee = get_object_or_404(Applicant, id=employee_id)                                     
                    employee.delete()
                    return redirect('employees') 
                if action_type == 'edit':
                    employee = get_object_or_404(Applicant, id=employee_id)
                    employee.save() 
                    return redirect('employment_application')           
    return redirect('employees')  

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})

def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_edit.html', {'form': form})

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_delete.html', {'task': task})

from django.shortcuts import render
from django.http import JsonResponse
from .models import product
from .serializers import productserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def productlist(request, format=None):
    if request.method == 'GET':
        pro = product.objects.all()
        serializer = productserializer(pro, many=True)
        return Response(serializer.data)
# forms.py
from django import forms
from .models import Applicant
from .models import PromotedEmployee 
from .models import Task
from .models import product

class EmploymentApplicationForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'  # Or specify the fields you want to include

class EmploymentApplicationForm(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__' 

class PromotedEmployeesform(forms.ModelForm):
    class Meta:
        model = PromotedEmployee
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'taskname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'taskdescription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'date_of_submission': forms.TextInput(attrs={'class': 'form-control'}),
        }

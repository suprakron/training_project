from django import forms
from .models import Course,Employee

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name', 'description']



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_code', 'position', 'name', 'certificate']
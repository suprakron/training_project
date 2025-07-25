from django import forms
from .models import Course,Employee,TrainingRecord

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'employee_code': 'รหัสพนักงาน',
            'course_code': 'รหัสหลักสูตร',
            'course_name': 'ชื่อหลักสูตร',
            'course_detail': 'รายละเอียดหลักสูตร',
            'training_date': 'วันที่อบรม',
            'evidence_file': 'ไฟล์หลักฐานการอบรม (PDF)',
        }



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_code', 'position', 'name', 'certificate', 'photo', 'skills']
 
  


class TrainingRecordForm(forms.ModelForm):
    class Meta:
        model = TrainingRecord
        fields = ['employee', 'course',   'certificate']
        widgets = {
            'date_completed': forms.DateInput(attrs={'type': 'date'}),
        }
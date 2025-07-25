from django.db import models
from django.utils.timezone import now


# models.py
class Employee(models.Model):
    employee_code = models.CharField(max_length=50, unique=False, default='')
    position = models.CharField(max_length=50) 
    name = models.CharField(max_length=100)
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)
    photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee_code} - {self.name}"



class Course(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    hours = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return f'{self.code} - {self.name}'

def today_date():
    return now().date()
 
class TrainingRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='trainings')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    certificate = models.FileField(upload_to='certificates/', blank=True, null=True)
    passed = models.BooleanField(default=False) 
    date = models.DateField(default=today_date)
 
 

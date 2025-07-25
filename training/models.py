from django.db import models

# models.py
class Employee(models.Model):
    employee_code = models.CharField(max_length=20, unique=True)
    position = models.CharField(max_length=50)  # เป็นแค่ข้อความตำแหน่ง
    name = models.CharField(max_length=100)
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        return f"{self.employee_code} - {self.name}"



class Course(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.code} - {self.name}'

class TrainingRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='trainings')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    certificate = models.FileField(upload_to='certificates/')

    def __str__(self):
        return f'{self.employee.name} - {self.course.name}'

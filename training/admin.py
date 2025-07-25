from django.contrib import admin
from .models import Employee, Course, TrainingRecord

admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(TrainingRecord)

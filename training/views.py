from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Course, TrainingRecord
from .forms import CourseForm,EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib import messages

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "เพิ่มพนักงานเรียบร้อยแล้ว")
                return redirect('index')
            except IntegrityError:
                messages.error(request, "รหัสพนักงานนี้มีอยู่ในระบบแล้ว")
        else:
            messages.error(request, "กรุณากรอกข้อมูลให้ถูกต้อง")
    else:
        form = EmployeeForm()
    return render(request, 'training/add_employee.html', {'form': form})



def index(request):
    employees = Employee.objects.all()
    return render(request, 'training/index.html', {'employees': employees})
 
# หน้ารายละเอียดพนักงาน: ดูหลักสูตรที่อบรม
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    trainings = employee.trainings.select_related('course')
    return render(request, 'training/employee_detail.html', {
        'employee': employee,
        'trainings': trainings
    })

 

def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_manage')
    else:
        form = CourseForm()
    return render(request, 'training/course_form.html', {'form': form, 'title': 'เพิ่มหลักสูตร'})

def course_edit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_manage')
    else:
        form = CourseForm(instance=course)
    return render(request, 'training/course_form.html', {'form': form, 'title': 'แก้ไขหลักสูตร'})

def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_manage')
    return render(request, 'training/course_confirm_delete.html', {'course': course})


def course_manage(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('name')
        description = request.POST.get('description')
        if code and name:
            Course.objects.create(code=code, name=name, description=description)
        return redirect('course_manage')

    courses = Course.objects.all()
    return render(request, 'training/course_manage.html', {'courses': courses})


@csrf_exempt
def delete_course(request, course_id):
    if request.method == 'POST':
        Course.objects.filter(id=course_id).delete()
    return redirect('manage_courses')
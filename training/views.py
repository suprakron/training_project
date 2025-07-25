from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Course, TrainingRecord
from .forms import CourseForm, EmployeeForm, TrainingRecordForm
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.contrib import messages
from collections import namedtuple


def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "เพิ่มพนักงานเรียบร้อยแล้ว")
                return redirect("index")
            except IntegrityError:
                messages.error(request, "รหัสพนักงานนี้มีอยู่ในระบบแล้ว")
        else:
            messages.error(request, "กรุณากรอกข้อมูลให้ถูกต้อง")
    else:
        form = EmployeeForm()
    return render(request, "training/add_employee.html", {"form": form})


def employee_edit(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "อัปเดตข้อมูลพนักงานเรียบร้อยแล้ว")
                return redirect("index")
            except IntegrityError:
                messages.error(request, "รหัสพนักงานซ้ำกับที่มีอยู่ในระบบ")
        else:
            messages.error(request, "กรุณากรอกข้อมูลให้ถูกต้อง")
    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        "training/edit_employee.html",
        {
            "form": form,
            "employee": employee,
        },
    )


def index(request):
    employees = Employee.objects.all()
    courses = Course.objects.all()
    return render(
        request,
        "training/index.html",
        {
            "employees": employees,
            "courses": courses,
        },
    )


def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    trainings = TrainingRecord.objects.filter(employee=employee).select_related(
        "course"
    )
    return render(
        request,
        "training/employee_detail.html",
        {
            "employee": employee,
            "trainings": trainings,
        },
    )

 

def course_add(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CourseForm()
    return render(
        request, "training/course_form.html", {"form": form, "title": "เพิ่มหลักสูตร"}
    )


def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CourseForm(instance=course)

    return render(
        request, "training/edit_course.html", {"form": form, "course": course}
    )


def employee_delete(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == "POST" or request.method == "GET":
        employee.delete()
        return redirect("index")


def course_manage(request):
    if request.method == "POST":
        code = request.POST.get("code")
        name = request.POST.get("name")
        description = request.POST.get("description")
        if code and name:
            Course.objects.create(code=code, name=name, description=description)
        return redirect("index")

    courses = Course.objects.all()
    return render(request, "training/course_manage.html", {"courses": courses})


@csrf_exempt
def delete_course(request, course_id):
    if request.method == "POST":
        Course.objects.filter(id=course_id).delete()
    return redirect("course_manage")


def add_training(request):
    if request.method == 'POST':
        form = TrainingRecordForm(request.POST, request.FILES)
        if form.is_valid():
            training = form.save()  
            return redirect('employee_detail', employee_id=training.employee.id)  
    else:
        form = TrainingRecordForm()
    return render(request, 'training/add_training.html', {'form': form})




def edit_training(request, training_id):
    training = get_object_or_404(TrainingRecord, id=training_id)
    if request.method == "POST":
        form = TrainingRecordForm(request.POST, request.FILES, instance=training)
        if form.is_valid():
            form.save()
            return redirect("employee_detail", employee_id=training.employee.id)
    else:
        form = TrainingRecordForm(instance=training)
    return render(
        request, "training/edit_training.html", {"form": form, "training": training}
    )

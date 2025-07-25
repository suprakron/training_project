from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path("employee/<int:employee_id>/edit/", views.employee_edit, name="employee_edit"),
    path('employee/delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('courses/', views.course_manage, name='course_manage'),
     path('edit-course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete-course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('add-training/', views.add_training, name='add_training'),
    path('edit/<int:training_id>/', views.edit_training, name='edit_training'),
     

]

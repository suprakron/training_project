from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),

    path('courses/', views.course_manage, name='course_manage'),
    path('courses/add/', views.course_add, name='course_add'),
    path('courses/edit/<int:course_id>/', views.course_edit, name='course_edit'),
    path('courses/delete/<int:course_id>/', views.course_delete, name='course_delete'),
    path('delete-course/<int:course_id>/', views.delete_course, name='delete_course'),
]

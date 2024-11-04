from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.list_employees, name='list_employees'),
    path('employees/create/', views.create_employee, name='create_employee'),
    path('employees/<int:pk>/', views.retrieve_employee, name='retrieve_employee'),
    path('employees/<int:pk>/update/', views.update_employee, name='update_employee'),
    path('employees/<int:pk>/delete/', views.delete_employee, name='delete_employee'),
]

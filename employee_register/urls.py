
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),    #get & post request for insert operation
    path('<int:id>/', views.employee_form, name="employee_update"),   #get & post request for update operation
    path('delete/<int:id>/', views.employee_delete, name="employee_delete"),
    path('list/', views.employee_list, name='employee_list')    #get request to retrieve and display all records
]

# giving names for url is better option
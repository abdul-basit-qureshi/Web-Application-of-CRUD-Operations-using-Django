from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.

def employee_list(request):
    context = {'employee_list':Employee.objects.all()}  #getting all data of employee class
    return render(request, 'employee_register/employee_list.html', context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id==0:       #if it is an insert operation, it will be an empty form
            form = EmployeeForm()
        else:   
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_register/employee_form.html', {'form': form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():     # if form is filled and then submitted
            form.save()
        return redirect('/employee/list')   # form will save in this address


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
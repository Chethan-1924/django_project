from django.http import HttpResponse
from employees.models import Employee
from django.shortcuts import render


def home(request):

    # fetch the data from the employee tables
    # we need access to that to work with that
    employees = Employee.objects.all()   # this brigns all the data from the employee table
    # print(employees)  # Query Set

    context = {
        "employees" : employees
    }
    # return HttpResponse("Employee Records - Chethan Kumar")
    # return HttpResponse(employees)
    return render(request, "home.html", context)
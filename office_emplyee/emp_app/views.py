from django.shortcuts import render, HttpResponse
from .models import Department, Role, Employee
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        "emps":emps,
    }
    print(context)
    return render(request, 'all_emp.html', context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(fname__icontains=name)| Q(lname__icontains = name))
        if dept:
            emps = emps.filter(dept_name =dept)
        if role:
            emps = emps.filter(role_name = role)

        context = {
            'emps':emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method== 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An exception occur')


def add_emp(request):
    if request.method == 'POST':
        first_name =request.POST['fname']
        last_name = request.POST['lname']
        salary = request.POST['salary']
        address = request.POST['address']
        city_name = request.POST['city_name']
        new_emp = Employee(fname=first_name, lname=last_name, salary=salary, address=address, city_name=city_name)
        print(new_emp)
        new_emp.save()
        return HttpResponse('Employee added successfully')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('An excetion occur')

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee removed successfully')
        except:
            return HttpResponse('Please enter a valid id')
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)
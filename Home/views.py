from django.shortcuts import render
from django.http import HttpResponse


from.models import employee


# Create your views here.
def index(request):
    
    employees = employee.objects.all()
    
    details = {
        'employee':employees
        
           
    }
    
    
    return render(request,'Home/index.html',details)


def add_employee(request):
    if request.method=='POST':
        name= request.POST.get('name')
        age= request.POST.get('age')
        address= request.POST.get('address')
        employees=employee(name=name, age=age, address=address)
        employees.save()
        
        return HttpResponse("Employee Added Successfully")
    else:
        return render(request,'Home/add_employee.html')


def update_employee(request,id):
    employees=employee.objects.get(pk=id) 
    if request.method=='POST':
        name= request.POST.get('name')
        age= request.POST.get('age')
        address= request.POST.get('address')
        
        employees.name=name
        employees.age=age
        employees.address=address
        
        employees.save()
        
        return HttpResponse("Employee Updated Successfully")
    else:
        return render(request,'Home/add_employee.html',{'employee':employee})
                
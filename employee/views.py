from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import employeeform
from .models import employee
# Create your views here.
def Home(request):
    form=employeeform()
    if request.method=='POST':
        form=employeeform(request.POST)
        form.save()
        form=employeeform()
    
    data=employee.objects.all()

    


    context={
        'form':form,
        'data':data,
    }
    return render(request,'employee/index.html',context)

# Delete View
def Delete_record(request,id):
    a=employee.objects.get(pk=id)
    a.delete()
    return redirect('/')
    

# Update View
def Update_Record(request,id):
    if request.method=='POST':
        data=employee.objects.get(pk=id)
        form=employeeform(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:

        data=employee.objects.get(pk=id)
        form=employeeform(instance=data)
    context={
        'form':form,
    }
    return render (request,'employee/update.html',context)
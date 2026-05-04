from django.shortcuts import render,redirect
from app1.forms import  EmployeeForm,DepartmentForm,searchform,SearchFormAuto
# Create your views here.
from app1.models import Employee,Department
from django.db.models import ProtectedError,Q
from django.contrib import messages
def add_emp(request):
    if request.method=='POST':
        f=EmployeeForm(request.POST)
        if f.is_valid():
            try:
                data=f.cleaned_data
                new=f.save()
                f=EmployeeForm()
                messages.success(request, f"Employee onboarding complete! Name: {data['name']} (ID: {new.emp_id})")
            except Exception:
                messages.error(request, "Database Sync Error: Unable to save employee details. Please contact IT support.")
        return render(request,'addemp.html',{'f':f})
    f=EmployeeForm()
    return render(request,'addemp.html',{'f':f})

def add_def(request):
    if request.method=='POST':
        f=DepartmentForm(request.POST)
        if f.is_valid():
            try:
                data=f.cleaned_data
                f.save()
                f=DepartmentForm()
                messages.success(request, "New department has been successfully registered in the system.")
            except Exception:
                messages.error(request, "Operation Failed: Unable to create department. Please try again.")
        return render(request,'dep.html',{'f':f})
    f=DepartmentForm()
    return render(request,'dep.html',{'f':f})
def dashboard(request):
    try:
        total_dep=Department.objects.count()
        total_emp=Employee.objects.count()
        return render(request,'dashboard.html',{'emp':total_emp,'dep':total_dep})
    except Exception:
        messages.warning(request, 'System Alert: Unable to fetch real-time dashboard statistics.')
    return render(request,'dashboard.html')



def update_view(request):
    if request.method=='GET':
        f=searchform()
        response=render(request,'updateform.html',{'f':f})
        return response
    else:
        try:

            f=searchform(request.POST)
            if f.is_valid():
                eid=f.cleaned_data['Employee_id']
                try:
                    emp=Employee.objects.get(emp_id=eid)
                    return redirect('edit',id=emp.emp_id)
                except Employee.DoesNotExist:
                    messages.error(request, f'Record Not Found: No employee exists with ID {eid}.')
                    return render(request,'updateform.html',{'f':f})
            else:
                return render(request,'updateform.html',{'f':f})
        except ValueError:
            messages.error(request,'Please Enter Only Digit')
        except Exception:
            messages.error(request, "Search Error: We're unable to process your request at this time.")
    return render(request,'updateform.html',{'f':f})
def edit(request,id):
    find=Employee.objects.get(emp_id=id)
    if request.method=='POST':
        f=EmployeeForm(request.POST,instance=find)
        if f.is_valid():
            try:
                f.save()
                messages.success(request, f'Update Successful: Details for {find.name} have been modified.')
                return redirect('dash')
            except Exception:
               messages.error(request, "Update Failed: Could not save the changes. Please verify the data.")
    else:
        f=EmployeeForm(instance=find)

    return render(request,'addemp.html',{'f':f})
def emp_list(request):
    try:
        f=Employee.objects.all()
        return render(request,'list.html',{'f':f})
    except Exception:
        messages.error(request, "Access Denied: Unable to retrieve employee directory.")
        return render(request,'list.html')
def delete(request, id):
    try:
        emp = Employee.objects.get(emp_id=id)
        emp.delete()
    except Exception:
        messages.error(request, "Delete Error: Could not remove the employee record.")
    return redirect('list_emp')
def view_dep(request):
    try:

        f=Department.objects.all()
        return render(request,'dep_list.html',{'f':f})
    except Exception:
            messages.error(request, "Fetch Error: Could not load department list.")
            return render(request,'dep_list.html')
def del_dep(request,id):
    try:
        emp=Department.objects.get(id=id)
        emp.delete()
        return redirect('list_dep')
    except ProtectedError:
        messages.error(request, "Action Blocked: This department has active employees. Please reassign them before deletion.")
        return redirect('list_dep')
def edit_dep(request,id):
    emp=Department.objects.get(id=id)
    if request.method=='POST':
        f=DepartmentForm(request.POST,instance=emp)
        if f.is_valid():
            f.save()
            messages.success(request, f'Department "{emp.dep_name}" updated successfully.')
            return redirect('dash')
    else:
        f=DepartmentForm(instance=emp)
    return render(request,'dep.html',{'f':f})
def search(request):
    if request.method=='GET':
        f=SearchFormAuto()
        return render(request,'search.html',{'f':f})
    else:
        f=SearchFormAuto(request.POST)
        if f.is_valid():
            data=f.cleaned_data['user_input']
            user_dep=f.cleaned_data['dep']
            result=Employee.objects.filter((Q(name__icontains=data)| Q(phone__icontains=data)| Q(email__icontains=data)))
            if user_dep:
                result=Employee.objects.filter(dep=user_dep)
            return render(request,'search.html',{'f':f,'result':result,'user_input':data,'user_dep':user_dep})
        return render(request,'search.html',{'f':f})
    


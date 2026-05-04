import re
from django import forms
from app1.models import Department,Employee
from datetime import date,timedelta
def dep_name_error(value):
    value=value.strip()
    if not re.fullmatch(r'[a-zA-Z ]+',value):
        raise forms.ValidationError('Special characters or numbers are not allowed. Use letters only.')
class DepartmentForm(forms.ModelForm):
    dep_name = forms.CharField(validators=[dep_name_error],widget=forms.TextInput(attrs={'placeholder': 'e.g. Human Resources', 'class': 'form-control'}))
    class Meta:
        model=Department
        fields='__all__'
def name_error(value):
    value=value.strip()

    if len(value) < 2:
        raise forms.ValidationError('Name is too short. It must be at least 2 characters.')

    if not re.fullmatch(r'[A-Za-z ]+', value):
        raise forms.ValidationError('Invalid Name. Only alphabets and spaces are allowed.')

def mobile_error(value):
    value=value.strip()
    if not re.fullmatch(r'[6-9][0-9]{9}', value):
        raise forms.ValidationError('Please enter a valid 10-digit Indian mobile number starting with 6-9.')
    if len(set(value)) == 1:
        raise forms.ValidationError('This looks like a dummy number. Please enter a valid mobile number.')
def salary_error(value):
    try:
        value = float(value)
    except:
        raise forms.ValidationError('Invalid format. Please enter salary in numbers (e.g., 25000.00).')
    if value <= 0:
        raise forms.ValidationError('Salary must be a positive amount greater than 0.')
def hire_date_error(value):
    today=date.today()

    one_month_before=today-timedelta(days=30)
    one_month_after=today+timedelta(days=30)
    if value > one_month_after:
        raise forms.ValidationError(f'Future date limit exceeded. Max allowed: {one_month_after.strftime("%d-%b-%Y")}')
    elif value < one_month_before:
       raise forms.ValidationError(f'Backdated entry limit exceeded. Min allowed: {one_month_before.strftime("%d-%b-%Y")}')



class EmployeeForm(forms.ModelForm):
    name=forms.CharField(validators=[name_error],
                        widget=forms.TextInput(attrs={'placeholder':'Full Name (as per ID)'}))
    phone=forms.CharField(validators=[mobile_error],
                        widget=forms.TextInput(attrs={'placeholder':'+91 XXXXX XXXXX'}))
    salary=forms.CharField(validators=[salary_error]
                        ,widget=forms.TextInput(attrs={'placeholder':'Amount in INR'}))
    hire_date=forms.DateField(validators=[hire_date_error],
                              widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model=Employee
        fields='__all__'

class searchform(forms.Form):
    Employee_id=forms.CharField(label='Search by ID...',widget=forms.TextInput(attrs={'placeholder':'Enter Employee ID'}))
class SearchFormAuto(forms.Form):
    user_input = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Search by Name, Email or Mobile...'}))
    dep=forms.ModelChoiceField(required=False,queryset=Department.objects.all())
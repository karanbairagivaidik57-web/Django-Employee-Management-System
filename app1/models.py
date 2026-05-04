from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=50,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='department'
    def __str__(self):
        return self.dep_name
class Employee(models.Model):
    emp_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=60,unique=True)
    phone=models.CharField(max_length=15)
    salary=models.DecimalField(max_digits=12,decimal_places=2)
    hire_date=models.DateField()
    dep=models.ForeignKey(Department,on_delete=models.PROTECT)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='employee'

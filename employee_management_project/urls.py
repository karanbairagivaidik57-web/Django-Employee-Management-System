"""
URL configuration for employee_management_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import add_emp,add_def,dashboard, update_view,edit,emp_list,delete,view_dep,del_dep,edit_dep,search
urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/',add_emp,name='emp'),
    path('dep/',add_def,name='dep'),
    path('',dashboard,name='dash'),
    path('update/', update_view,name='up'),
    path('edit_page/<int:id>/',edit,name='edit'),
    path('list/',emp_list,name='list_emp'),
    path('delete_emp/<int:id>/',delete,name='delete_emp'),
    path('view_dep/',view_dep,name='list_dep'),
    path('delete/<int:id>/',del_dep,name='delete_dep'),
    path('edit/<int:id>/',edit_dep,name='edit_dep'),
    path('search/',search,name='search')
]

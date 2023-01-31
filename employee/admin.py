from django.contrib import admin
from .models import employee

# Register your models here.
class employeeadmin(admin.ModelAdmin):
    list_display=['Name', 'Email', 'Password']


admin.site.register(employee,employeeadmin)


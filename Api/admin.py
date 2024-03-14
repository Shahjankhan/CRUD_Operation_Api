from django.contrib import admin
from .models import student
# Register your models here.

@admin.register(student)
class Admin_student(admin.ModelAdmin):
    list_display=['id','name','roll','city']

from django.contrib import admin
from .models import *
# Register your models here.


class Display_batch(admin.ModelAdmin):
    list_display=['Batch_name']

class Display_Dept(admin.ModelAdmin):
    list_display=['Dept_name']

class Display_sem(admin.ModelAdmin):
    list_display=['sem']

class Display_student(admin.ModelAdmin):
    list_display=['student_name','dept','sem','batch']

admin.site.register(Batch, Display_batch)
admin.site.register(Department,Display_Dept)
admin.site.register(Semester,Display_sem)
admin.site.register(Student,Display_student)
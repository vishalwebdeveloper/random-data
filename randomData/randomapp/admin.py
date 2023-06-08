from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(student)
admin.site.register(record)

class Student(admin.ModelAdmin):
    list_display = ['id','roll','name','city']

class record(admin.ModelAdmin):
    list_display = ['id','roll','name','city']
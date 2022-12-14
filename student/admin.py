from django.contrib import admin
from .models import student


@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['schoolId', 'standardId', 'id', 'email',
                    'name', 'password']

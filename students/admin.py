from django.contrib import admin

# Register your models here.
from .models import Student


class StudentAdmin(admin.ModelAdmin):

    # Form to add student should only include fields name, last name, username, and password
    fields = ('name', 'last_name', 'username', 'password')


admin.site.register(Student, StudentAdmin)

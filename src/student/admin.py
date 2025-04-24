from django.contrib import admin
from student.models import Students

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user','classe')

admin.site.register(Students,StudentAdmin)
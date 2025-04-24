from django.contrib import admin
from tutor.models import Tutors

# Register your models here.

class TutorAdmin(admin.ModelAdmin):
    list_display = ('user','phone_number','student')
    model = Tutors
    
admin.site.register(Tutors,TutorAdmin)
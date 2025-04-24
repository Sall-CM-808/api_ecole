from django.contrib import admin
from professor.models import Professors

# Register your models here.

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('user','subject','level')
    model = Professors
    
admin.site.register(Professors,ProfessorAdmin)
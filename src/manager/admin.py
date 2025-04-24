from django.contrib import admin
from manager.models import SchoolManagers
# Register your models here.


class SchoolManagerAdmin(admin.ModelAdmin):
    list_display = ('user','poste','phone_number')
    model = SchoolManagers
    
    
admin.site.register(SchoolManagers,SchoolManagerAdmin)
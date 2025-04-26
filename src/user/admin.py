from django.contrib import admin
from user.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','email','role']
    model = User
    
admin.site.register(User,UserAdmin)


from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(User)


# class UserAdmin(admin.ModelAdmin):
#     list_display= (
#         'id',
#         'first_name',
#         'last_name',
#         'email',        
#     )  

admin.site.site_header = "Welcome to Library Admin Portal"
admin.site.site_title = ""
admin.site.index_title = "Admin Portal"



from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Add option fields to built-in fields username, password and password2
    # (confirm password) in the UserAdmin class
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Optional Fields', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
        }),
    )

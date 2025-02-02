from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User


class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'phoneNumber', 'name', 'is_student', 'is_company', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'phoneNumber', 'name', 'is_student', 'is_company', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    list_display = ['email', 'username', 'phoneNumber',
                    'name', 'is_student', 'is_company']
    search_field = ('email', 'username')
    ordering = ('email',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

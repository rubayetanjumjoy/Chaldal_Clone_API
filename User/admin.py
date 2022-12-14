from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .models import Address

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email','gender','date_of_birth', 'password','phone_number','is_otp_verified','otp', 'name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email','phone_number', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email','phone_number','gender','is_otp_verified', 'name', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User,UserAdmin)
admin.site.register(Address)
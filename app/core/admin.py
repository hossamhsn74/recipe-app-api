from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from django.utils.translation import gettext as _


class AdminUser(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password')}),
        (_('Permissions'), {
         'fields': ('is_active', 'is_superuser', 'is_staff')}),
        (_('dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':
            ('first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )


admin.site.register(CustomUser, AdminUser)

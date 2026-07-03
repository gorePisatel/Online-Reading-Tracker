from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import register

from apps.users.models import CustomUser


@register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'role',
        'is_staff',
        'is_active',
    )
    search_fields = ('email', 'username','first_name', 'last_name')
    list_filter = ('role', 'is_staff', 'is_active')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
            'fields': (
                'username',
                'first_name',
                'last_name',
                'avatar',
                'bio',
            ),
        }),
        (_('Role'), {'fields': ('role',)}),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'password1',
                'password2',
                'role',
                'is_active',
                'is_staff',
            ),
        }),
    )

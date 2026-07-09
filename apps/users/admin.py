from django.contrib.admin import ModelAdmin, register
from django.contrib.auth.admin import UserAdmin

from apps.users.models import CustomUser, UserSettings


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
    search_fields = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('role', 'is_staff', 'is_active')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': (
                'username',
                'first_name',
                'last_name',
                'avatar',
                'bio',
            ),
        }),
        ('Role', {'fields': ('role',)}),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
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


@register(UserSettings)
class UserSettingsAdmin(ModelAdmin):
    list_display = (
        'user',
        'theme',
        'is_private',
        'notifications_enabled',
        'created_at',
        'updated_at',
    )
    search_fields = ('user__email', 'user__username')
    list_filter = ('theme', 'is_private', 'notifications_enabled')

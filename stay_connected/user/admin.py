from django.contrib import admin
from user.models import User, Avatar


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "rating",
        "my_answers",
        "avatar",
    )
    list_filter = (
        "rating",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email"
    )
    filter_horizontal = (
        'groups',
        'user_permissions'
    )
    fieldsets = [
        ('Personal Info', {
            'fields': [
                'first_name', 'last_name', 'email', 'password'
            ],
        }),
        ('Statistics', {
            'fields': ['rating', 'my_answers']
        }),
        ('Permissions', {
            'fields': ['is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions']
        }),
        ('Important Dates', {
            'fields': ['date_joined', 'last_login']
        }),
    ]


@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from user.models import User, Avatar


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    pass

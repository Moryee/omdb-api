from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'username', 'email', 'is_staff')

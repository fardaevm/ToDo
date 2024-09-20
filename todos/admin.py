from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from todos.models import CustomUser, Todo


@admin.register(CustomUser)
class CustomUserAdmin(DefaultUserAdmin):
    pass


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)


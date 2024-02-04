from django.contrib import admin
from .models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class UserResources(resources.ModelResource):
    class Meta:
        model = User


class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("username", "id", "email", "is_staff", "is_superuser", "is_active")
    resource_class = UserResources
    search_fields = ["username"]


admin.site.register(User, UserAdmin)

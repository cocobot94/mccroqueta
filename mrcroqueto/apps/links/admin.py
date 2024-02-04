from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Link


# Register your models here.
class LinkResources(resources.ModelResource):
    class Meta:
        model = Link


class LinkAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("description", "url")
    resource_class = LinkResources


admin.site.register(Link, LinkAdmin)

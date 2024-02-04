from django.contrib import admin
from apps.blog.models import Post, CategoryPost, Comments


# Register your models here.
class postAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "vistas")
    list_display = (
        "title",
        "id",
        "author",
        "vistas",
        "category_post",
        "state",
        "created",
    )


class CommentsAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)
    list_display = ("user", "post")


class CategoryPostAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)


admin.site.register(Post, postAdmin)
admin.site.register(CategoryPost, CategoryPostAdmin)
admin.site.register(Comments, CommentsAdmin)

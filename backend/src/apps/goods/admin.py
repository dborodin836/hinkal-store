from django.contrib import admin
from django.utils.html import format_html

from .models import Comment, Dish, Category


class DishAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        """Adds a nice little circle with image of dish."""
        return format_html(f'<img src="{obj.image.url}" width="40" style="border-radius: 50px" />')

    thumbnail.short_description = "photo"  # type: ignore

    list_display = ("id", "title", "thumbnail", "created_at", "added_by")

    list_display_links = (
        "id",
        "title",
    )

    search_fields = (
        "title",
        "added_by",
    )

    list_filter = ("added_by",)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "dish",
        "parent",
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Dish, DishAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)

from django.contrib import admin
from django.utils.html import format_html

from .models import Dish


class DishAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px" />'.format(object.image.url))

    thumbnail.short_description = 'photo'

    list_display = (
        'id',
        'title',
        'thumbnail',
        'added_date',
        'added_by'
    )

    list_display_links = (
        'id',
        'title',
    )

    search_fields = (
        'title',
        'added_by',
    )

    list_filter = (
        'added_by',
    )


admin.site.register(Dish, DishAdmin)

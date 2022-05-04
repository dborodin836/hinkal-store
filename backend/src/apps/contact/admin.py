from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):

    list_display = ("id", "subject", "email", "added_date")

    list_display_links = ("subject", "id")

    search_fields = ("subject", "message", "email", "name")

    list_filter = ("email", "added_date")


admin.site.register(Contact, ContactAdmin)

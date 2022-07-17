from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):

    list_display = ("id", "subject", "email", "created_at")

    list_display_links = ("subject", "id")

    search_fields = ("subject", "message", "email", "name")

    list_filter = ("email", "created_at")


admin.site.register(Contact, ContactAdmin)

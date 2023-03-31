from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Customer, Vendor


class VendorAdmin(BaseUserAdmin):
    """Admin representation for Vendor"""

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("company_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


class CustomerAdmin(BaseUserAdmin):
    """Admin representation for Customer"""

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "email", "phone", "address")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vendor, VendorAdmin)

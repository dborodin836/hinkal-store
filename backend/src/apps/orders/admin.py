from django.contrib import admin

from .models import Discount, Order, OrderItem, OrderModifier


class OrderItemAdmin(admin.ModelAdmin):
    """Order item representation in django admin panel"""

    list_display = ("id", "item", "amount")


class OrderItemInline(admin.TabularInline):
    """Inline class for easier adding a products"""

    model = OrderItem
    extra = 3


class OrderAdmin(admin.ModelAdmin):
    """Order representation in django admin panel"""

    list_display = (
        "id",
        "ordered_by",
        "created_at",
    )
    inlines = (OrderItemInline,)


class DiscountAdmin(admin.ModelAdmin):
    """Discount representation in django admin panel"""

    list_display = (
        "discount_word",
        "discount_amount",
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(OrderModifier)

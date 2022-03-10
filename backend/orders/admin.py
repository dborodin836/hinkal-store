from django.contrib import admin

from .models import Order, OrderItem, Discount


class OrderAdmin(admin.ModelAdmin):
    """Order representation in django admin panel"""

    list_display = (
        'id',
        'ordered_by',
        'ordered_date',
    )


class OrderItemAdmin(admin.ModelAdmin):
    """Order item representation in django admin panel"""

    list_display = (
        'id',
        'item',
        'amount'
    )


class DiscountAdmin(admin.ModelAdmin):
    """Discount representation in django admin panel"""

    list_display = (
        'discount_word',
        'discount_amount',
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Discount, DiscountAdmin)

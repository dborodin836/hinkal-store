from django.contrib import admin

from .models import CustomUser, Countries, UserAddress


class CountriesAdmin(admin.ModelAdmin):
    pass


class UserAddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(UserAddress, UserAddressAdmin)

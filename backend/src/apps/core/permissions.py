from rest_framework import permissions


class VendorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if str(request.user).lower() == "vendor":
            return True
        if request.method.lower() in ["get", "head", "options", "trace"]:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return True

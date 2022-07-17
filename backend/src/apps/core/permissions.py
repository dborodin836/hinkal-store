from rest_framework import permissions


class Author(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user.id, obj.added_by.id, "esx")
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.id == obj.added_by.id:
            return True
        return False

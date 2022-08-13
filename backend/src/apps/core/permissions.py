from rest_framework import permissions
from logging import getLogger

logger = getLogger("main")


class Author(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        res = request.user.id == obj.ordered_by.id
        logger.debug(f"Author permission = {res}")
        return request.user.id == obj.ordered_by.id

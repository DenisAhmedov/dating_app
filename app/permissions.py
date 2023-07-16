from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsClientOrAdmin(BasePermission):
    """
    Просмотр участников разрешен всем, редактирование только админу и самому участнику.
    """

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user.is_staff or
            obj.id == request.user.id
        )

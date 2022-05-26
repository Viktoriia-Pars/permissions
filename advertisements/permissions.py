from rest_framework.permissions import BasePermission


class IsOwnerOnly(BasePermission):
    message = 'Only owner allowed'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator

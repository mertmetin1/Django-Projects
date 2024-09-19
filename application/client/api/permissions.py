from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
   
        # Admins and staff members have full access.
        if request.user and (request.user.is_staff or request.user.is_superuser):
            return True
   
        # Read permissions are allowed to any request.
        # So we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj == request.user



class IsSuperuserOrStaff(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff))

from rest_framework import permissions

class OwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Superuser check
        if request.user.is_superuser:
            return True
        # Check if the request user is the owner of the blog
        return request.user == obj.blogger_user



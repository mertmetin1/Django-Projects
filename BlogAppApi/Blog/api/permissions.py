from rest_framework import permissions

class OwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True


        # Superuser check
        if request.user.is_superuser:
            return True

        # Check if the request user is the owner of the blog
        return request.user == obj.blog_owner.blogger_user

class VerifiedBloggerPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

                # Superuser check
        if request.user.is_superuser:
            return True

        # Check if the request user is a verified blogger
        if hasattr(request.user, 'blogOwnerUser'):
            return request.user.blogOwnerUser.blogger_IsVerified
        
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Superuser check
        if request.user.is_superuser:
            return True

        # Check if the request user is the owner of the blog and is verified
        return request.user == obj.blog_owner.blogger_user and obj.blog_owner.blogger_IsVerified
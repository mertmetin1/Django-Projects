from rest_framework import permissions




class KendiProfiliYaDaReadOnly(permissions.BasePermission):
    
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
    

        return request.user == obj.user
    
    
    
class DurumSahibiYaDaReadOnly(permissions.BasePermission):
    
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        

        return request.user.profil == obj.user_profil
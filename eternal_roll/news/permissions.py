from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # если метод безопасный(чтение) то всем пользователям
            return True
        
        return bool(request.user and request.user.is_staff) # иначе только админу
    
class IsOwnerOrReadOnly(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user   # если юзер из БД равен юзеру который пришел с запросом то true
    

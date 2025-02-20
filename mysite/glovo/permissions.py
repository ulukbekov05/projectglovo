from rest_framework import permissions


class CheckUserProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'owner':
            return True
        return False

class CheckUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'client':
            return True
        return False

class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
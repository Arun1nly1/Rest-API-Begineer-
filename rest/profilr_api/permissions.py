from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    'Allow user to edit their own profile'

    def has_object_permission(self, request, view, obj):
        'Checks user is trying to edit their own profile'
        if request.method in permissions.SAFE_METHODS:
            return True
    
        if (obj.id == request.user.id):
            return True      
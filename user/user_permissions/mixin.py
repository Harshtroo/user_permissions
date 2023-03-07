from django.contrib.auth.mixins import PermissionRequiredMixin


class MyCustomPermissions(PermissionRequiredMixin):
    
    def has_permission(self):
        user_permissions = self.request.user.get_all_permissions()
        # print(self.request.user.has_permission(self.permission_required))
        # print(user_permissions)
        # print( self.permission_required)
        permissions_required = []
        for i in self.permission_required:
            if i in user_permissions:
                permissions_required.append(True)
            else:
                permissions_required.append(False)
        # print(permissions_required)
        # print(all(permissions_required))
        if self.request.user.is_authenticated and all(permissions_required):
            return True
        return False
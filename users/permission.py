from rest_framework import permissions
from rest_framework.views import View, Request


class IsEmployeeOrSameUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.user.is_employee:
            return True
        return request.user.is_employee or (
            request.user.id == view.kwargs.get("user_id")
        )

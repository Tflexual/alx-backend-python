from django.http import HttpResponseForbidden

class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_paths = ['/chats/admin/']
        if any(request.path.startswith(path) for path in restricted_paths):
            user = request.user
            if not (user.is_authenticated and (user.is_staff or user.is_superuser)):
                return HttpResponseForbidden("You do not have permission to access this page")
        return self.get_response(request)

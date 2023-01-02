from django.middleware.common import MiddlewareMixin
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def maintenance_mode_active(user):
    return not user.is_staff


class MaintenanceMiddleware(MiddlewareMixin):
    # Set the flag to False by default
    maintenance_mode = False

    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        if self.maintenance_mode:
            # Set a flag in the request object to indicate that the site is in maintenance mode
            request.maintenance_mode = True
            return redirect('maintenance')

    @classmethod
    def toggle_maintenance_mode(cls):
        cls.maintenance_mode = not cls.maintenance_mode

    def __call__(self, request):
        response = self.get_response(request)
        return response
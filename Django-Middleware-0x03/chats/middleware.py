from datetime import datetime
import logging

# Setup logger
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('requests.log')
formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        response = self.get_response(request)
        return response


from django.http import HttpResponseForbidden

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        if request.path.startswith('/chats/') and not (18 <= current_hour < 21):  # 6PM-9PM
            return HttpResponseForbidden("Chat is only available from 6PM to 9PM")
        return self.get_response(request)



from time import time

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.message_log = {}  # {ip: [timestamps]}

    def __call__(self, request):
        if request.method == 'POST' and request.path.startswith('/chats/'):
            ip = request.META.get('REMOTE_ADDR')
            now = time()
            timestamps = self.message_log.get(ip, [])

            # Remove timestamps older than 1 minute
            timestamps = [t for t in timestamps if now - t < 60]
            if len(timestamps) >= 5:
                return HttpResponseForbidden("Message limit exceeded. Try again later.")

            timestamps.append(now)
            self.message_log[ip] = timestamps

        return self.get_response(request)





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






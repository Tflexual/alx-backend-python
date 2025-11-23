from datetime import datetime
from django.http import HttpResponseForbidden

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        if request.path.startswith('/chats/') and not (18 <= current_hour < 21):  # 6PM-9PM
            return HttpResponseForbidden("Chat is only available from 6PM to 9PM")
        return self.get_response(request)

from django.shortcuts import redirect
from django.contrib import messages

LOGIN_EXEMPT_URLS = [
    '/',
    '/login/'
]


class First:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in LOGIN_EXEMPT_URLS:
            messages.warning(request, 'please login first')
            return redirect('home:login')
        response = self.get_response(request)

        return response

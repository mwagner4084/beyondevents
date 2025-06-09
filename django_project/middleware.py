from django.http import HttpResponsePermanentRedirect

class RedirectToWwwMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host == 'beyondeventsllc.com':
            return HttpResponsePermanentRedirect(f'https://www.beyondeventsllc.com{request.get_full_path()}')
        return self.get_response(request)

from django.utils.deprecation import MiddlewareMixin

class myMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("Get参数: ", request.GET.get("a"))
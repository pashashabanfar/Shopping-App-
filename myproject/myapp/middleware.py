from django.http import HttpResponse
class MiddleWareLifeCycle:
    def __init__(self, get_response):
        print('INIT')
        self.get_response = get_response
    def __call__(self, request):
        print('Before view executed')
        response = self.get_response(request)
        print('After view executed')
        return response

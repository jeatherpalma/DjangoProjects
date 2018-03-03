from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello to my first app with Django")
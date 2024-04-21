from django.shortcuts import render # noqa
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == "POST":
        return HttpResponse('You must have <strong>posted</strong> something.')
    else:
        return HttpResponse(request.method)

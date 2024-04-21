from django.shortcuts import render # noqa
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello,world! My first' \
                        'Django app... but not the last!")

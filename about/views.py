from django.shortcuts import render # noqa
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello,world! My SECOND \
                        Django app... this one is called = 'About \
                        <br>Here's a link back - <a href='/'>LINK</a>")

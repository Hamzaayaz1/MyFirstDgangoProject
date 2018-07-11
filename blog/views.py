#from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import datetime
def today_is(request):
    now = datetime.datetime.now()
    html = "<html><body>Current date and time: {0}</body></html>".format(now)
    return HttpResponse(html)

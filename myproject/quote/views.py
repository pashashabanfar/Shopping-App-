from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def quote(Request):
    return HttpResponse("this is quote function")



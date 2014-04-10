from django.shortcuts import render
from  django.http import HttpResponse
import pysolr
# Create your views here.

def home(request):
    return HttpResponse("HOME PAGE")


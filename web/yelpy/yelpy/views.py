from django.shortcuts import render, get_object_or_404
from django.http import *

def index(request):
	return render(request, 'yelpy/index.html')
def profile(request):
	return render(request,'yelpy/profile.html')
def search2(request):
	return render(request,'yelpy/search2.html')

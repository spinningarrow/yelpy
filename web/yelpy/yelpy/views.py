from django.shortcuts import render, get_object_or_404
from django.http import *

def index(request):
	return render(request, 'yelpy/index.html')
def profile(request):
	return render(request,'yelpy/profile.html')
def search2(request):
	return render(request,'yelpy/search2.html')
def form(request):
	if request.method == 'POST':
		form = foodForm(request.POST)
		if form.is_valid():
			chinese = form.cleaned_data['chinese']
			indian = form.cleaned_data['indian']
			vietnamese = form.cleaned_data['vietnamese']
			thai = form.cleaned_data['thai']
			western = form.cleaned_data['western']
			return render(request, 'yelpy/landing.html', {
				'chinese': chinese, 'indian':indian, 'vietnamese':vietnamese,'thai':thai,'western':western,
			})
			
	else:        
		form = foodForm()

	return render(request, 'yelpy/profile.html', {
		'form': form,
	})

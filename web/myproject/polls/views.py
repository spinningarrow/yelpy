from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Question
from polls.forms import AuthorForm
from django.contrib.auth.decorators import login_required


def detail(request, poll_id):
	poll = get_object_or_404(Question, pk=poll_id)
	return render(request, 'polls/details.html', {'poll': poll})

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)

def index(request):
	latest_poll_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_poll_list': latest_poll_list}
	return render(request, 'polls/index.html', context)

#@login_required
def form(request):
	if request.method == 'POST':
		form = AuthorForm(request.POST)
		if form.is_valid():
			nom = form.cleaned_data['name']
			title = form.cleaned_data['title']
			return render(request, 'polls/landing.html', {
				'name': nom, 'title':title,
			})
			
	else:        
		form = AuthorForm()

	return render(request, 'polls/form.html', {
		'form': form,
	})

#@login_required
def landing(request):	
	return render(request, 'polls/landing.html')
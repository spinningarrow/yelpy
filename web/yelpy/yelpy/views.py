from django.shortcuts import render, get_object_or_404
from django.http import *
from yelpy.forms import *
from django.views.decorators.csrf import csrf_exempt
from yelpy.models import User
from django.core import serializers
import json
import logging

logger = logging.getLogger(__name__)
globvar = 123
def index(request):
    return render(request, 'yelpy/index.html')

# @csrf_exempt
# def get_user_id(request):
#     if request.method == 'POST':
#         global globvar
#         globvar = request.POST.get('id', '')


@csrf_exempt
def profile(request):
    if request.method == 'POST':
        form = AllForm(data=request.POST)
        # print form.errors
        if form.is_valid():
            form.save()

        else:

            # chinese = form.cleaned_data['chinese']
            # indian = form.cleaned_data['indian']
            # vietnamese = form.cleaned_data['vietnamese']
            # thai = form.cleaned_data['thai']
            # western = form.cleaned_data['western']
            userId = request.POST.get('id', '')
            obj = All.objects.get(id=userId)

            obj.chinese = request.POST.get('chinese', '')
            obj.indian = request.POST.get('indian', '')
            obj.vietnamese = request.POST.get('vietnamese', '')
            obj.thai = request.POST.get('thai', '')
            obj.western= request.POST.get('western', '')
            obj.fitness = request.POST.get('fitness', '')
            obj.golf = request.POST.get('golf', '')
            obj.football = request.POST.get('football', '')
            obj.swimming = request.POST.get('swimming', '')
            obj.fishing = request.POST.get('fishing', '')
            obj.clothes = request.POST.get('clothes', '')
            obj.accessories = request.POST.get('accessories', '')
            obj.women = request.POST.get('women', '')
            obj.children = request.POST.get('children', '')
            obj.men = request.POST.get('men', '')
            obj.gifts = request.POST.get('gifts', '')
            obj.gallery = request.POST.get('gallery', '')
            obj.cinema = request.POST.get('cinema', '')
            obj.theater = request.POST.get('theater', '')


            obj.save()

            # return render(request, 'yelpy/profile.html', {
            #   'chinese': chinese, 'indian':indian, 'vietnamese':vietnamese,'thai':thai,'western':western,
            # })
        return HttpResponse(json.dumps(form.data), content_type="application/json")

    else:
        form = AllForm()


    return render(request, 'yelpy/profile.html', {
        'form': form,
    })
    #return render(request,'yelpy/profile.html')
def search2(request):
    return render(request,'yelpy/search2.html')
def form(request):
    if request.method == 'POST':
        form = AllForm(request.POST)
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
        form = AllForm()

    return render(request, 'yelpy/profile.html', {
        'form': form,
    })


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        global globvar
        id = request.POST.get('id', '')
        #globvar = id
        name = request.POST.get('name', '')
        users = User.objects.filter(id=id)

        if len(users) == 0: # User doesn't exist, create one
            user_object = User(id = id, name = name)
            user_object.save()
            users = User.objects.filter(id=id)
            return HttpResponse(json.dumps(users[0].as_dict()), content_type="application/json")

        return HttpResponse(json.dumps(users[0].as_dict()), content_type="application/json")

    users = User.objects.all()
    return HttpResponse(json.dumps(users[0].as_dict()), content_type="application/json")

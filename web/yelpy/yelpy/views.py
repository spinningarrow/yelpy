from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import *
from yelpy.forms import *
from django.views.decorators.csrf import csrf_exempt
from yelpy.models import User
from django.core import serializers
from django.forms.models import model_to_dict
import json
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'yelpy/index.html', {
        'fb_id': request.session.get('fb_user_id', '')
    })

@csrf_exempt
def profile(request):
    if request.method == 'POST':
        form = AllForm(data=request.POST)
        if form.is_valid():
            form.save()

        else:
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
            messages.info(request, "Success! Check your personalised results at the <a href=\"http://localhost:8000/automaticquery/\">Search</a> page.")
            obj.save()

    else: # not a POST request
        userId = request.session.get('fb_user_id', '')
        user_prefs_data = None

        if userId:
            user_objects = All.objects.filter(id=userId)
            if len(user_objects):
                user_prefs_data = model_to_dict(user_objects[0])

        form = AllForm(data=user_prefs_data)

    return render(request, 'yelpy/profile.html', {
        'form': form,
    })

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

    return render(request, 'yelpy/profile.html', {
        'form': form,
    })


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        id = request.POST.get('id', '')
        name = request.POST.get('name', '')
        users = User.objects.filter(id=id)

        session_fb_id = request.session.get('fb_user_id', '')

        if session_fb_id != id:
            request.session['fb_user_id'] = id

        if len(users) == 0: # User doesn't exist, create one
            user_object = User(id = id, name = name)
            user_object.save()
            # users = User.objects.filter(id=id)
            return HttpResponse(json.dumps("Created user and logged in."), content_type="application/json")

        return HttpResponse(json.dumps("Logged in."), content_type="application/json")

    # users = User.objects.all()
    return HttpResponse(json.dumps("Who should I log in?"), content_type="application/json")

def logout(request):
    fb_user_id = request.session.get('fb_user_id', '')
    if fb_user_id:
        request.session.flush()

    return HttpResponse(json.dumps("Logged out, if there was anyone logged in."), content_type="application/json")

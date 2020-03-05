# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Projects, User, UpdateInfo
from .forms import SubscriptionForm

# Create your views here.

def index(request):
    return render(request, 'BrianWeb/index.html')

def about(request):
    return render(request, 'BrianWeb/about.html')

def portfolio(request):
    portfolio = Projects.objects.all()
    #update_info = UpdateInfo.objects.all()
    user_info = User.objects.all()

    portfolio_dict = {
        'portfolio': portfolio,
        'user': user_info,
    }

    return render(request, 'BrianWeb/portfolio.html', context=portfolio_dict)

def contact(request):
    form = SubscriptionForm()
    return render(request, 'BrianWeb/contact.html', {'form' : form})

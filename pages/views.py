from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from market.models import Generator
from django.db.models import Sum
from django.core import serializers
import pandas as pd
import json


def about(request):
    return render(request, 'coming_soon.html', {})


def home_view2(request):
    return render(request, 'page7345315.html', {})


def home_view(request):
    return render(request, 'page7361961.html', {})
    # return HttpResponseRedirect('https://wuadigital.tilda.ws/')


def error_404_view(request, exception):
    return render(request, 'coming_soon.html')

# df_filler()

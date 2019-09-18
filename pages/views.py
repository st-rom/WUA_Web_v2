from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from market.models import Generator
from django.db.models import Sum
from django.core import serializers
import pandas as pd
import json


def home_view(request):
    # return HttpResponse("<h2>HH</h2>")
    return render(request, 'https://akoganalyst.wixsite.com/wua2019', {})


def about(request):
    return render(request, 'coming_soon.html', {})


def home_page(request):
    return HttpResponseRedirect('https://wuadigital.tilda.ws/')


def error_404_view(request, exception):
    return render(request, 'coming_soon.html')

# df_filler()

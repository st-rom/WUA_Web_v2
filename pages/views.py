from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from market.models import Generator
from django.db.models import Sum
from django.core import serializers
import pandas as pd
import json
from . import models


def about(request):
    return render(request, 'coming_soon.html', {})


def home_view2(request):
    # return render(request, 'page7345315.html', {})
    return render(request, 'landing_ua.html', {})


def home_view(request):
    return render(request, 'page7361961.html', {})
    # return HttpResponseRedirect('https://wuadigital.tilda.ws/')


def error_404_view(request, exception):
    return render(request, 'coming_soon.html')

# df_filler()
# class IndexView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)
#         context['page_list'] = models.Page.objects.all()
#         return context

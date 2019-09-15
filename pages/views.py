from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from market.models import Generator
from django.db.models import Sum
from django.core import serializers
import pandas as pd
import json


def home_view(request):
    # return HttpResponse("<h2>HH</h2>")
    return render(request, 'https://akoganalyst.wixsite.com/wua2019', {})


def market_list(request):
    posts = Generator.objects.order_by('-tonnes_total')[:9]
    # print(posts)
    return render(request, 'market_find.html', {'posts': posts})
    # return render(request, 'base.html', {})


def market_create(request):
    return render(request, 'coming_soon.html', {})


def analytics_graph(request):
    return render(request, 'analiz_big-graph.html', {})


def gen_detail(request, pk):
    gen = get_object_or_404(Generator, pk=pk)
    return render(request, 'gen_details.html', {'gen': gen})


def analytics_map(request):
    return render(request, 'analiz_map.html', {})


def analytics_other(request):
    # posts = Generator.objects.all()
    # posts = Generator.objects.aggregate(Sum('tonnes_total'))
    posts = {**Generator.objects.aggregate(Sum('tonnes_1')), **Generator.objects.aggregate(Sum('tonnes_2')), **Generator.objects.aggregate(Sum('tonnes_3')), **Generator.objects.aggregate(Sum('tonnes_4'))}
    # posts_serialized = serializers.serialize('json', posts)
    posts_serialized = json.dumps(posts)
    return render(request, 'analiz_other.html', {'p_s': posts_serialized})


def about(request):
    return render(request, 'coming_soon.html', {})


def error_404_view(request, exception):
    return render(request, 'coming_soon.html')

# df_filler()

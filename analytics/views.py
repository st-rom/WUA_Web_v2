from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from market.models import Generator
from django.db.models import Sum
from django.core import serializers
import pandas as pd
import json


def analytics_graph(request):
    return render(request, 'analiz_big-graph.html', {})


def analytics_map(request):
    return render(request, 'analiz_map.html', {})


def analytics_other(request):
    posts_all = Generator.objects.all()
    # posts = Generator.objects.aggregate(Sum('tonnes_total'))
    posts = {**Generator.objects.aggregate(Sum('tonnes_1')), **Generator.objects.aggregate(Sum('tonnes_2')), **Generator.objects.aggregate(Sum('tonnes_3')), **Generator.objects.aggregate(Sum('tonnes_4'))}
    posts_serialized2 = serializers.serialize('json', posts_all)
    posts_serialized = json.dumps(posts)
    # posts_serialized2 = json.dumps(posts_all)
    return render(request, 'analiz_other.html', {'p_s': posts_serialized, 'all_data': posts_serialized2})

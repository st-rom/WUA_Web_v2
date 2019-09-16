from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from market.models import Generator


def market_list(request):
    posts = Generator.objects.order_by('-tonnes_total')[:9]
    # print(posts)
    return render(request, 'market_find.html', {'posts': posts})
    # return render(request, 'base.html', {})


def market_create(request):
    return render(request, 'coming_soon.html', {})


def gen_detail(request, pk):
    gen = get_object_or_404(Generator, pk=pk)
    return render(request, 'gen_details.html', {'gen': gen})

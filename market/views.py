from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from market.models import Generator
from django import template
from django.core import serializers
from django_pandas.io import read_frame
import pandas as pd


register = template.Library()
waste_code_explanations = ['Загальна сума кількості відходів в тоннах, незалежно від класу небезпеки',
                           'Показник загального утворення відходів (ПЗУВ) - критерій обсягу утворення відходів, що '
                           'розраховується за формулою Пзув = 5000 х М1 + 500 х М2 + 50 х М3 + 1 х М4, де М1, М2, М3,'
                           ' М4 - маса в тонах відходів 1, 2, 3 та 4 класів небезпеки відповідно',
                           'Надзвичайно небезпечні речовини', 'Високонебезпечні речовини',
                           'Помірно небезпечні речовини', 'Безпечні речовини']
waste_explanation_ending = '. Клас небезпеки відходів встановлюється залежно від вмісту в них високотоксичних речовин' \
                           ' розрахунковим методом або згідно з переліком відходів, наведених у Державному' \
                           ' класифікаторі відходів. На всі види відходів розробляється технічний паспорт згідно з ' \
                           'Міждержавним стандартом ДСТУ-2195-93, дія якого поширюється на 10 країн СНД. '


def market_list(request, page=1):
    page = 1 if page < 1 else page
    all_gens = len(Generator.objects.all())
    posts = Generator.objects.order_by('-tonnes_total')[(page - 1) * 12:(page - 1) * 12 + 12]
    # print(posts)
    return render(request, 'market_list.html', {'posts': posts, 'page_num': page, 'all_gens_num': all_gens})
    # return render(request, 'base.html', {})
    # return redirect('market_list', page=page)


def market_create(request):
    return render(request, 'coming_soon.html', {})


def market_find(request, page=1, search=''):
    page = 1 if page < 1 else page
    all_gens = Generator.objects.all()
    posts = Generator.objects.order_by('-tonnes_total')[(page - 1) * 12:(page - 1) * 12 + 12]
    # df = read_frame(all_gens)
    df = pd.read_csv("static/data/declarations_full.csv", sep=';')
    # options = list(df['trash_name'].unique())
    # options = [s for s in trash_types if search.lower() in s.lower()]
    options = [(r['code'], r['trash_name']) for i, r in df[['code', 'trash_name']].drop_duplicates().iterrows()]

    # print(posts)
    # ser_posts = serializers.serialize('json', posts)
    return render(request, 'market_find.html', {'posts': posts, 'page_num': page, 'all_gens_num': len(all_gens),
                                                'all_posts': serializers.serialize('json', all_gens), 'options': options})


def gen_detail(request, pk):
    gen = get_object_or_404(Generator, pk=pk)
    return render(request, 'gen_details.html', {'gen': gen, 'tooltip': waste_code_explanations,
                                                'tooltip_ending': waste_explanation_ending})

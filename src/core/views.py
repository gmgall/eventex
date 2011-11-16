# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from random import choice

def homepage(request):
    quotes = (
        {'quote': 'O melhor evento da paróquia', 'credit': 'John Doe'},
        {'quote': 'Tão bom que quase parece fictício', 'credit': 'Jane Doe'},
    )
    context = RequestContext(request, choice(quotes))
    return render_to_response('index.html', context)

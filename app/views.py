from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    # template = loader.get_template('gaurang.html')
    template = loader.get_template('app/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
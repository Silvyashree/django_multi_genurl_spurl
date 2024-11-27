from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def T3_lite(request):
    return HttpResponse ('<h1> T3 Lite 5G </h1>')

def Y200_5G(request):
    return HttpResponse ('<h1> vivo y20 5g </h1>')
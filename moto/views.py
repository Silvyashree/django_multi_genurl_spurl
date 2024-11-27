from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def edge (request):
    return HttpResponse ( ' <h1> Motorola Edge 50 Pro 5G with 68W Charger (Luxe Lavender, 256 GB </h1>')

def ultra (request):
    return HttpResponse ('<h1>motorola edge 50 ultra  </h1>')


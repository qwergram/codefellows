from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Card

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're viewing cards")

def detail(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'cardapp/showcard.html', {'card': card})

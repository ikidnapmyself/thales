from django.shortcuts import render
from django.http import JsonResponse
from . import spacy


def home(request):
    return render(request, 'index.html')


def process(request):
    sentence = request.POST['sentence']
    return JsonResponse(spacy.process(sentence))

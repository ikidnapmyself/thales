from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

from . import spacy


def home(request):
    return render(request, 'index.html')


@csrf_protect
def process(request):
    sentence = request.POST['sentence']
    return JsonResponse(spacy.process(sentence))

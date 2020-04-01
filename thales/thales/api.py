from django.http import JsonResponse
from oauth2_provider.decorators import protected_resource
from . import spacy


@protected_resource(scopes=['process'])
def process(request):
    sentence = request.POST['sentence']
    return JsonResponse(spacy.process(sentence))

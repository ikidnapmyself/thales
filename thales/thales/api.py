from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.decorators import protected_resource
from . import spacy


@csrf_exempt
@protected_resource(scopes=['process'])
def process(request):
    sentence = request.POST['sentence']
    return JsonResponse(spacy.process(sentence))

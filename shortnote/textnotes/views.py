from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from shortnote.textnotes.models import TextNote
from shortnote.textnotes.serializers import TextSerializer


def new_textnote(request):
    return HttpResponse(content='OK NEW', status=HTTP_200_OK)


def get_textnote(request):
    return HttpResponse(content='OK GET', status=HTTP_200_OK)


def get_all_textnote(request):
    return HttpResponse(content='OK GEL ALL', status=HTTP_200_OK)


def post_textnote(request):
    return HttpResponse(content='OK POST', status=HTTP_200_OK)


def get_json_textnote_by_id(request, textnote_id):
    try:
        textnote = TextNote.objects.get(pk = textnote_id)
        textnote_serializer = TextSerializer(instance=textnote)
        return JsonResponse(data=textnote_serializer.data)
    except ObjectDoesNotExist:
        return JsonResponse({'status': 'text note not found'}, status=HTTP_404_NOT_FOUND)

def get_json_textnote_by_id(request, textnote_id):
    try:
        textnote = TextNote.objects.get(pk = textnote_id)
        textnote_serializer = TextSerializer(instance=textnote)
        return JsonResponse(data=textnote_serializer.data)
    except ObjectDoesNotExist:
        return JsonResponse({'status': 'text note not found'}, status=HTTP_404_NOT_FOUND)

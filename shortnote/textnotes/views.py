from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED

from shortnote.textnotes.models import TextNote
from shortnote.textnotes.serializers import TextNoteSerializer


def new_textnote(request):
    return HttpResponse(content='OK NEW', status=HTTP_200_OK)


def get_textnote(request):
    return HttpResponse(content='OK GET', status=HTTP_200_OK)


def get_all_textnote(request):
    return HttpResponse(content='OK GEL ALL', status=HTTP_200_OK)


def post_textnote(request):
    return HttpResponse(content='OK POST', status=HTTP_200_OK)


def get_json_textnote_by_user(request, user_id):
    try:
        textnotes = TextNote.objects.filter(owner=user_id)
        textnotes_serializer = TextNoteSerializer(textnotes, many=True)
        return JsonResponse(data=textnotes_serializer.data,safe=False)
    except BaseException as err:
        return JsonResponse({'Error': str(err)}, status=HTTP_404_NOT_FOUND)


def get_json_textnote_by_id(request, textnote_id):
    try:
        textnote = TextNote.objects.get(pk = textnote_id)
        textnote_serializer = TextNoteSerializer(instance=textnote)
        return JsonResponse(data=textnote_serializer.data)
    except BaseException as err:
        return JsonResponse({'Error': str(err)}, status=HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['POST'])
def post_json_textnote(request):
    try:
        textnote_serializer = TextNoteSerializer(data=request.data)
        textnote_serializer.is_valid()
        textnote_serializer.save()
        return JsonResponse({'status': 'TextNote saved successfully'}, status=HTTP_201_CREATED)
    except BaseException as err:
        return JsonResponse({'Error': str(err)})

from django.http.response import HttpResponse
from rest_framework.status import HTTP_200_OK


def new_textnote(request):
    return HttpResponse(content='OK NEW', status=HTTP_200_OK)

def get_textnote(request):
    return HttpResponse(content='OK GET', status=HTTP_200_OK)

def get_all_textnote(request):
    return HttpResponse(content='OK GEL ALL', status=HTTP_200_OK)

def post_textnote(request):
    return HttpResponse(content='OK POST', status=HTTP_200_OK)

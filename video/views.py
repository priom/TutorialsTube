from django.shortcuts import render
from django.template.response import TemplateResponse
from video.models import Video


def video(request):
    data = Video.objects.all().order_by('pk')
    return TemplateResponse(request, 'index.html', {"data": data})

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Dawki, Krowy, Krycia, GrupyZywieniowe
from .serializers import KrowySerializer, DawkiSerializer, KryciaSerializer, GrupyZywienioweSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the stadoBaza index.")
# Create your views here.
@csrf_exempt
def dawki_list(request):
    if request.method == 'GET':
        dawki = Dawki.objects.all()
        serializer = DawkiSerializer(dawki, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer = DawkiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return  JsonResponse(serializer.errors,status=400)
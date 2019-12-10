from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Dawki, Krowy, Krycia, GrupyZywieniowe
from .serializers import KrowySerializer, DawkiSerializer, KryciaSerializer, GrupyZywienioweSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the stadoBaza index.")
# Create your views here.
@api_view(['GET', 'POST'])
def dawki_list(request, format=None):
    if request.method == 'GET':
        dawki = Dawki.objects.all()
        serializer = DawkiSerializer(dawki, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = DawkiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def dawki_detail(request, pk, format=None):
    try:
        dawki = Dawki.objects.get(pk=pk)
    except Dawki.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DawkiSerializer(dawki)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DawkiSerializer(dawki, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = DawkiSerializer(dawki, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dawki.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def grupyZywieniowe_list(request, format=None):
    if request.method == 'GET':
        grupyZywieniowe = GrupyZywieniowe.objects.all()
        serializer = GrupyZywienioweSerializer(grupyZywieniowe, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = GrupyZywienioweSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def grupyZywieniowe_detail(request, pk, format=None):
    try:
        grupyZywieniowe = GrupyZywieniowe.objects.get(pk=pk)
    except GrupyZywieniowe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GrupyZywienioweSerializer(grupyZywieniowe)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GrupyZywienioweSerializer(grupyZywieniowe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = GrupyZywienioweSerializer(grupyZywieniowe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        grupyZywieniowe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def krowy_list(request, format=None):
    if request.method == 'GET':
        krowy = Krowy.objects.all()
        serializer = KrowySerializer(krowy, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = KrowySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def krowy_detail(request, pk, format=None):
    try:
        krowy = Krowy.objects.get(pk=pk)
    except Krowy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = KrowySerializer(krowy)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = KrowySerializer(krowy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = KrowySerializer(krowy, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        krowy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def krycia_list(request, format=None):
    if request.method == 'GET':
        krycia = Krycia.objects.all()
        serializer = KryciaSerializer(krycia, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = KryciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def krycia_detail(request, pk, format=None):
    try:
        krycia = Krycia.objects.get(pk=pk)
    except Krycia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = KryciaSerializer(krycia)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = KryciaSerializer(krycia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = KryciaSerializer(krycia, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        krycia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


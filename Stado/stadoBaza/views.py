from django.http import Http404

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView

from .serializers import Userserializer

from .models import Dawki, Krowy, Krycia, GrupyZywieniowe
from .serializers import KrowySerializer, DawkiSerializer, KryciaSerializer, GrupyZywienioweSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

def index(request):
    return HttpResponse("Hello, world. You're at the stadoBaza index.")
# Create your views here.
class dawki_list(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
            dawki = Dawki.objects.all()
            serializer = DawkiSerializer(dawki, many=True)
            return Response(serializer.data)
    def post (self, request, format=None):
            serializer = DawkiSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class dawki_detail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            dawki = Dawki.objects.get(pk=pk)
            return dawki
        except Dawki.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request,pk, format=None):
        dawki=self.get_object(pk)
        serializer = DawkiSerializer(dawki)
        return Response(serializer.data)

    def put(self, request,pk, format=None):
        dawki = self.get_object(pk)
        serializer = DawkiSerializer(dawki, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,pk, format=None):
            dawki = self.get_object(pk)
            serializer = DawkiSerializer(dawki, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
            dawki = self.get_object(pk)
            dawki.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class grupyZywieniowe_list(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        grupyZywieniowe = GrupyZywieniowe.objects.all()
        serializer = GrupyZywienioweSerializer(grupyZywieniowe, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GrupyZywienioweSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)  # bez owner=self.request.user nie widzi ownera
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class grupyZywieniowe_detail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            grupyZywieniowe = GrupyZywieniowe.objects.get(pk=pk)
            return grupyZywieniowe
        except GrupyZywieniowe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



    def get(self, request, pk, format=None):
        grupyZywieniowe = self.get_object(pk)
        serializer = GrupyZywienioweSerializer(grupyZywieniowe)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        grupyZywieniowe = self.get_object(pk)
        serializer = GrupyZywienioweSerializer(grupyZywieniowe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        grupyZywieniowe = self.get_object(pk)
        serializer = GrupyZywienioweSerializer(grupyZywieniowe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        grupyZywieniowe = self.get_object(pk)
        grupyZywieniowe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class krowy_list(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        krowy = Krowy.objects.all()
        serializer = KrowySerializer(krowy, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = KrowySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)                                                # bez owner=self.request.user nie widzi ownera
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class krowy_detail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            krowy = Krowy.objects.get(pk=pk)
            return krowy;
        except Krowy.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        krowy = self.get_object(pk)
        serializer = KrowySerializer(krowy)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        krowy = self.get_object(pk)
        serializer = KrowySerializer(krowy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk, format=None):
        krowy = self.get_object(pk)
        serializer = KrowySerializer(krowy, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        krowy = self.get_object(pk)
        krowy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class krycia_list(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        krycia = Krycia.objects.all()
        serializer = KryciaSerializer(krycia, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KryciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class krycia_detail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            krycia = Krycia.objects.get(pk=pk)
            return krycia
        except Krycia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        krycia = self.get_object(pk)
        serializer = KryciaSerializer(krycia)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        krycia = self.get_object(pk)
        serializer = KryciaSerializer(krycia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        krycia = self.get_object(pk)
        serializer = KryciaSerializer(krycia, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        krycia = self.get_object(pk)
        krycia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render
from rest_framework import viewsets
from main.models import Ad, Rubric, User
from .serializers import UserSerializer, RubricSerializer, AdsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RubricViewSet(viewsets.ModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer


class AdsViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer

from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from main.models import Ad, Rubric, User
from .serializers import UserSerializer, RubricSerializer, AdsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RubricViewSet(viewsets.ModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer


class AdsViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer

    def queryset_user(self):
        queryset = self.queryset
        queryset_user = queryset.filter(user=self.request.user)
        return queryset_user

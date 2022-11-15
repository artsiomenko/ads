from rest_framework import viewsets, generics, filters
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from main.models import Rubric, User
from .serializers import UserSerializer, RubricSerializer, AdsSerializer
from .services.queryset_params_for_ads import queryset_ads


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RubricViewSet(viewsets.ModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer


class AdsListViewSet(generics.ListAPIView):
    serializer_class = AdsSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'content']

    def get_queryset(self):
        return queryset_ads(self)

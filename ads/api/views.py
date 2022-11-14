from rest_framework import viewsets, generics
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


class AdsListAPIView(generics.ListAPIView):
    serializer_class = AdsSerializer

    def get_queryset(self):
        queryset = Ad.objects.all()
        rubric_id = self.request.query_params.get('rubric')
        if rubric_id is not None:
            queryset = queryset.filter(rubric__id=rubric_id)
        return queryset



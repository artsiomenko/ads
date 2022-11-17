from rest_framework import viewsets, generics
from main.models import Rubric, User, Ad
from .serializers import UserSerializer, RubricSerializer, AdsSerializer
from .services.AdsQueryParamsServices import AdsQueryParamsServices


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RubricViewSet(viewsets.ModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer


class AdsListFilterViewSet(generics.ListAPIView):
    serializer_class = AdsSerializer

    def get_queryset(self):
        return AdsQueryParamsServices().queryset_ads(self.request.query_params)


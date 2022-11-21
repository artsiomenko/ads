from rest_framework import viewsets, generics, mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.decorators import action
from main.models import Rubric, User, Ad
from .serializers import UserSerializer, AdsSerializer
from .services.AdsFilterServices import AdsFilterServices
from rest_framework.response import Response

from .services.AdsViewSetServices import AdsViewSetServices


class AdsViewSet(ModelViewSet):
    serializer_class = AdsSerializer

    def get_queryset(self):
        return AdsViewSetServices().queryset_ads(self.kwargs.get('pk'))

    @action(methods=['get'], detail=False)
    def rubric(self):
        return Response({'rubrics': [r.name for r in Rubric.objects.all()]})


class AdsListFilterViewSet(generics.ListAPIView):
    serializer_class = AdsSerializer

    def get_queryset(self):
        return AdsFilterServices().queryset_ads(self.request.query_params)

# class RubricViewSet(viewsets.ModelViewSet):
#     queryset = Rubric.objects.all()
#     serializer_class = RubricSerializer


# class AdViewSet(viewsets.ModelViewSet):
#     queryset = Ad.objects.all()
#     serializer_class = AdsSerializer

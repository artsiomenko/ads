from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from main.models import Rubric
from .serializers import AdsSerializer
from .services.AdsFilterServices import AdsFilterServices
from rest_framework.response import Response
from .services.AdsViewSetServices import AdsViewSetServices


class AdsViewSet(ModelViewSet):
    serializer_class = AdsSerializer

    def get_queryset(self):
        return AdsViewSetServices().queryset_ads(self.kwargs.get('pk'))

    @action(methods=['get'], detail=False)
    def rubric(self, request):
        rubric = Rubric.objects.all()
        return Response({r.name for r in rubric})


class AdsListFilterViewSet(generics.ListAPIView):
    serializer_class = AdsSerializer

    def get_queryset(self):
        return AdsFilterServices().queryset_ads(self.request.query_params)

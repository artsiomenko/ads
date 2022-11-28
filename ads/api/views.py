from django.http import Http404
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from main.models import Rubric, Ad
from .serializers import AdsSerializer, AdsUserSerializer
from rest_framework.response import Response
from .services.AdsViewSetServices import AdsViewSetServices


class AdsViewSet(ModelViewSet):
    serializer_class = AdsSerializer

    def get_queryset(self):
        return AdsViewSetServices().queryset_ads(self.kwargs.get('pk'), self.request.query_params)

    @action(methods=['get'], detail=False)
    def rubrics(self, request):
        return Response({r.name for r in Rubric.objects.all()})


class AdsListViewSet(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsUserSerializer
    permission_classes = (IsAdminUser | IsAuthenticatedOrReadOnly,)


class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdsUserSerializer
    lookup_url_kwarg = 'pk'
    queryset = Ad.objects.all()
    permission_classes = (IsAdminUser | IsAuthenticatedOrReadOnly,)

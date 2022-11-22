from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from main.models import Rubric
from .serializers import AdsSerializer
from rest_framework.response import Response
from .services.AdsViewSetServices import AdsViewSetServices


class AdsViewSet(ModelViewSet):
    serializer_class = AdsSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        return AdsViewSetServices().queryset_ads(self.kwargs.get('pk'), self.request.query_params)

    @action(methods=['get'], detail=False)
    def rubric(self, request):
        return Response({r.name for r in Rubric.objects.all()})

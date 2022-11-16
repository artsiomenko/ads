from .views import AdsListFilterViewSet, AdViewSet
from django.urls import path, include
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'ads', AdViewSet)

urlpatterns = [
    path('api/ads/', AdsListFilterViewSet.as_view(), name='ads-filters'),
    path('', include((router.urls, 'ads'))),
]
